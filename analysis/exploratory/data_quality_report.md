# Data Quality & Integrity Audit Report
**Dataset:** `Paytm_VOC_Authoritative_Final_Dataset.csv`  
**Total Records:** 113 Unique Respondents (`VIRTUS_001` to `VIRTUS_113`)  
**Audit Status:** Verified ($100\%$ Usable, $0$ Synthetic, $0$ Dropped Responses)

## 1. Quality Summary Metrics
| Audit Field | Value | Methodological Compliance |
| :--- | :--- | :--- |
| **Input Response Rows** | 113 | Complete census of submitted VOC responses |
| **Unique Respondent IDs** | 113 | 100% uniquely identified |
| **Duplicate Records** | 0 | 0 exact duplicate survey submissions |
| **Missing Demographic Fields** | 0 | 100% complete profile, city, frequency, occasions |
| **Clean Validated Records** | 110 (97.3%) | Clean, fully expressive responses |
| **Quality Review Flagged** | 3 (2.7%) | Placeholder verbatims ('na', 'No') on trigger question |

## 2. Specific Issues Identified & Actions Taken
1. **City Normalization:** Standardized raw strings (e.g. `'Sitapur '`, `'Sitapur'`, `'Lucknow '`, `'Bhopal '`, `'gurugram '`, `'Bangalore'`) into uniform naming while preserving original city location.
2. **Character Encoding:** Replaced Windows-1252/Unicode displacement artifacts (`815`, `cafs`) with proper clean punctuation (`8–15`, `cafés`).
3. **Placeholder Verbatims:** 3 records (`VIRTUS_001`, `VIRTUS_026`, `VIRTUS_027`) entered `'na'` or `'No'` for Question 11. These records are explicitly flagged in `Data_Quality_Flag` but kept in the dataset as their quantitative choices (apps, frequency, occasions, barriers) are 100% valid.
