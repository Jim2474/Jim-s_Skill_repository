# Textbook PDF Question Extraction

**Extracted:** 2026-05-19
**Context:** Extracting math exercise questions and answers from Chinese textbook PDFs using PyMuPDF

## Problem

Chinese math textbook PDFs have complex layouts where:
- Answer pages mix answers from previous and current chapters
- OCR text has character confusion (1O→10, l→1)
- Answer numbers are sequential across chapters but questions reset per chapter
- Question boundaries can have inverted y-coordinates

## Solution

### 1. Chapter Header Boundary Detection

Answer pages typically have this structure:
```
[Previous chapter answers at top]
第二章一元函数微分学        ← Chapter header
1.【解】(D).               ← Current chapter answers start here
2.【解】(C).
```

**Implementation:**
```python
def detect_answers(doc, chapter_num):
    found_chapter_header = False
    
    for pg_idx in range(config["answer_start"] - 1, config["answer_end"]):
        page = doc[pg_idx]
        blocks = parse_text_blocks(page)
        
        for block in blocks:
            # Detect chapter header
            if re.match(r'^第[一二三四五六七八九十]+章', block.text):
                found_chapter_header = True
                current_answer_no = 0
                answers = []  # Reset - discard previous chapter answers
                continue
            
            # Skip blocks before chapter header on first page
            if not found_chapter_header and pg_idx == config["answer_start"] - 1:
                continue
            
            # ... detect answer patterns
```

**Impact:** Without this, only 4-6 answers detected per chapter instead of 30-50.

### 2. OCR Number Normalization

PDF OCR confuses similar characters. Build a translation map:

```python
def _normalize_ocr_number(text: str) -> str:
    ocr_map = str.maketrans('OolISBGZ', '00115862')
    prefix = []
    for ch in text:
        if ch.isdigit() or ch in 'OolISBGZ':
            prefix.append(ch.translate(ocr_map))
        else:
            break
    rest = text[len(prefix):]
    return ''.join(prefix) + rest
```

**Common OCR confusions:**
| OCR reads | Actually is |
|-----------|-------------|
| O (letter) | 0 (digit) |
| l (lowercase L) | 1 (digit) |
| I (uppercase i) | 1 (digit) |
| S | 5 |
| B | 8 |
| G | 6 |
| Z | 2 |

### 3. Incremental Answer Numbering

PDF answer numbers are sequential across chapters:
- Chapter 1: answers 1, 2, 3, ..., 46
- Chapter 2: answers 47, 48, 49, ... (continues from 46)

But questions reset per chapter:
- Chapter 1: questions 1, 2, 3, ..., 46
- Chapter 2: questions 1, 2, 3, ..., 50

**Solution:** Use incremental numbering for answers:
```python
# WRONG: Uses absolute PDF number (47, 48, 49...)
answers.append(AnswerBoundary(question_no=a_num, ...))

# CORRECT: Uses incremental number (1, 2, 3...)
answer_seq = len(answers) + 1
answers.append(AnswerBoundary(question_no=answer_seq, ...))
```

### 4. Question-Number-Based Answer Matching

Index-based matching fails when answers are missing:
```python
# WRONG: Index-based (shifts all matches if answer missing)
for i, q in enumerate(questions):
    if i < len(answers):
        entry = generate_entry(q, answers[i])

# CORRECT: Question-number-based
answer_map = {a.question_no: a for a in answers}
for q in questions:
    answer = answer_map.get(q.question_no)
    if answer:
        entry = generate_entry(q, answer)
```

### 5. Crop Boundary Swap

Some question boundaries have y_end < y_start due to detection edge cases:
```python
y1 = max(0, int(question.y_start * scale) - padding)
y2 = min(img.height, int(question.y_end * scale) + padding)

# Handle edge case where y_end < y_start
if y2 < y1:
    y1, y2 = y2, y1
```

## Complete Pipeline

```python
# 1. Load PDF
doc = fitz.open(pdf_path)

# 2. For each chapter
for chapter_num in range(1, 7):
    # 3. Detect questions (incremental numbering)
    questions = detect_questions(doc, chapter_num)
    
    # 4. Detect answers (with chapter header boundary)
    answers = detect_answers(doc, chapter_num)
    
    # 5. Match by question number (not index)
    answer_map = {a.question_no: a for a in answers}
    
    # 6. Generate JSON entries
    for q in questions:
        answer = answer_map.get(q.question_no)
        if answer:
            entry = generate_question_entry(chapter_num, q, answer)
            
            # 7. Crop images (with boundary swap)
            crop_question_image(doc, q, output_path)
            crop_answer_image(doc, answer, output_path)
```

## When to Use

- Extracting questions from Chinese math textbook PDFs
- PDF has structured answer section at the end
- Answer pages mix content from multiple chapters
- OCR text quality is imperfect

## Key Configuration

```python
CHAPTER_CONFIG = {
    1: {
        "name": "第一章 函数 极限 连续",
        "question_start": 6,   # PDF page (1-indexed)
        "question_end": 22,
        "answer_start": 147,
        "answer_end": 157,
    },
    # ... more chapters
}
```

## Verification Checklist

- [ ] Answer counts match question counts per chapter (±2)
- [ ] All IDs are unique
- [ ] No y_end < y_start in boundaries
- [ ] Chapter headers detected in answer pages
- [ ] OCR normalization catches edge cases
