# A. Odd or Even?

## Problem Overview
This problem checks your understanding of basic number properties — specifically, determining whether a number is **odd** or **even**.

You are given multiple integers, and for each one, you must print a sentence stating whether the number is an **Odd number** or an **Even number**, following an exact output format.


## Input Format
- The first line contains an integer **T** — the number of test cases  
  (1 ≤ T ≤ 100)
- The next **T** lines each contain an integer **N**  
  (−10⁵ ≤ N ≤ 10⁵)

---

## Output Format
For each number **N**, print a line in the following format:

- `N is an Even number.`  
- `N is an Odd number.`  

**Note:**  
- Capitalization and punctuation **must match exactly**
- Each result must be printed on a **new line**

---

##  Example

### Input
5
10
19
7
3
100

### Output
10 is an Even number.
19 is an Odd number.
7 is an Odd number.
3 is an Odd number.
100 is an Even number.

## 🧠 Key Concept
A number is:
- **Even** if it is divisible by 2 → `N % 2 == 0`
- **Odd** otherwise

##  Forbidden Keywords
Do **NOT** use:
sort, open, file, creat(, fstream, thread,
process, system(, exec(


The provided solution avoids all forbidden keywords.

---

## 🛠 Language Used
- Python 3
- Compatible with Codeforces online judge