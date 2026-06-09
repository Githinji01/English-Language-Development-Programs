#  English Language Development (ELD) programs

**Automate, Track, and Optimize English Language Development (ELD) Programs**

*Inspired by Mt. Diablo Unified School District (August 2021 – August 2022): Designed and supported ELD programs for multilingual learners, implementing storytelling-based instructional strategies to improve student engagement and learning outcomes.*

---

##  **About This Toolkit**

This **Python-based toolkit** automates and optimizes **English Language Development (ELD) programs** for multilingual learners. It is designed to:

- **📚 Design ELD Programs**: Create and manage programs tailored to **grade levels, language focus, and storytelling strategies**.
- **📊 Track Student Engagement**: Monitor **engagement scores, language progress, and assessment outcomes**.
- **🎭 Optimize Storytelling Strategies**: Recommend and refine **instructional strategies** to maximize learning outcomes.
- **📈 Analyze Learning Outcomes**: Correlate **program effectiveness** with student growth and storytelling impact.

This toolkit is ideal for **ELD educators, school administrators, and curriculum designers** to **streamline program management** and **improve student success**.

---

##  **Why Use This Toolkit?**

### **For ELD Educators**

✅ **Design customized ELD programs** for diverse grade levels and language needs.  
✅ **Track student engagement** and identify at-risk learners.  
✅ **Optimize storytelling strategies** to enhance language acquisition.

### **For School Administrators**

✅ **Monitor program effectiveness** with data-driven reports.  
✅ **Allocate resources** based on engagement and outcome analysis.  
✅ **Ensure compliance** with standardized ELD program requirements.

### **For Curriculum Designers**

✅ **Refine instructional strategies** using outcome correlations.  
✅ **Scale successful programs** across grade levels and schools.  
✅ **Innovate with storytelling** to improve student engagement.

---

##  **Features**


| **Module**                          | **Description**                                                                          | **Key Functions**                          | **Output Example**                                                            |
| ----------------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------- |
| **ELD Program Designer**            | Designs and manages ELD programs for multilingual learners.                              | `design_program()`, `update_enrollment()`  | `{"program_id": "ELD001", "program_name": "Beginner ELD"}`                    |
| **Student Engagement Tracker**      | Tracks student engagement, language progress, and assessment scores.                     | `log_engagement()`, `analyze_engagement()` | `{"avg_engagement_score": "4.20", "at_risk_students": 2}`                     |
| **Storytelling Strategy Optimizer** | Optimizes storytelling-based instructional strategies for ELD programs.                  | `add_strategy()`, `recommend_strategies()` | `[{"strategy_name": "Picture Books", "effectiveness_score": 4.5}]`            |
| **Learning Outcome Analyzer**       | Analyzes and correlates learning outcomes with ELD programs and storytelling strategies. | `log_outcome()`, `analyze_outcomes()`      | `{"avg_growth": "18.50", "language_growth_distribution": {"Significant": 3}}` |


---

##  **Repository Structure**

```
English-Language-Development-Programs/
│── eld_program_toolkit.py        # Main script (all modules combined)
│
│
├── README.md                         # This file
└── LICENSE                           # MIT License
```

---

##  **Installation**

### **Prerequisites**

- Python 3.8+
- Required libraries: `pandas`, `numpy`

### **Setup**

1. Clone the repository:
  ```bash
   git clone https://github.com/Githinji01/English-Language-Development-Programs.git
   cd English-Language-Development-Programs
  ```
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```
3. Run the toolkit:
  ```bash
   python eld_program_toolkit.py
  ```

---

##  **Quick Start**

### **Run the Full Toolkit (Demo Mode)**

The main script (`eld_program_toolkit.py`) includes a **demo mode** that:

- Creates **sample data** if input files don’t exist.
- Lets you **test all modules** (1-6) interactively.

```bash
python eld_program_toolkit.py
```

**Example Output:**

```
🎓 Mt. Diablo Unified ELD Program Toolkit

Automate ELD Program Design, Student Engagement, and Learning Outcomes
================================================================================

Select a module to run:
1. 📚 ELD Program Designer
2. 📊 Student Engagement Tracker
3. 🎭 Storytelling Strategy Optimizer
4. 📈 Learning Outcome Analyzer
5. 📄 Generate All Reports
6. 🏃 Run All Modules (Demo)

Enter your choice (1-6): 6
```

### **Use Individual Modules**

Each module can be imported and used independently in your own scripts.

#### **1. ELD Program Designer**

```python
from scripts.eld_program_toolkit import ELDProgramDesigner

designer = ELDProgramDesigner()
program = designer.get_program_details("ELD001")
print(program)
# Output: {"program_id": "ELD001", "program_name": "Beginner ELD", ...}

new_program = designer.design_program(
    program_name="Advanced ELD for High School",
    target_grade_levels="9-12",
    language_focus="Spanish, Arabic, Vietnamese",
    start_date="2022-08-15",
    end_date="2023-06-15",
    instructors="Ms. Smith",
    storytelling_strategies="Debates, Presentations, Novel Studies"
)
print(new_program)
# Output: {"status": "Success", "program_id": "ELD004", ...}
```

#### **2. Student Engagement Tracker**

```python
from scripts.eld_program_toolkit import StudentEngagementTracker

tracker = StudentEngagementTracker()
engagement = tracker.analyze_engagement("ELD001")
print(engagement)
# Output: {"avg_engagement_score": "4.20", "at_risk_students": 2, ...}

at_risk = tracker.identify_at_risk_students()
print(at_risk)
# Output: [{"student_id": "STU002", "risk_reason": "Low engagement"}, ...]
```

#### **3. Storytelling Strategy Optimizer**

```python
from scripts.eld_program_toolkit import StorytellingStrategyOptimizer

optimizer = StorytellingStrategyOptimizer()
recommendations = optimizer.recommend_strategies(
    target_skills=["Speaking", "Confidence"],
    grade_level="K-5",
    budget="Low"
)
print(recommendations)
# Output: [{"strategy_name": "Role-Play", "effectiveness_score": 4.8}, ...]
```

#### **4. Learning Outcome Analyzer**

```python
from scripts.eld_program_toolkit import LearningOutcomeAnalyzer

analyzer = LearningOutcomeAnalyzer()
outcomes = analyzer.analyze_outcomes("ELD001")
print(outcomes)
# Output: {"avg_growth": "18.50", "language_growth_distribution": {"Significant": 3}, ...}

correlation = analyzer.correlate_strategies_with_outcomes("ELD001")
print(correlation)
# Output: {"program_name": "Beginner ELD", "avg_growth": "18.50", ...}
```

---

##  **Example Data**

The toolkit **automatically generates sample data** if input files don’t exist. Here’s what the sample data looks like:

### `**data/eld_programs.csv**`


| program_id | program_name     | target_grade_levels | language_focus    | start_date | end_date   | enrollment | instructors | storytelling_strategies          |
| ---------- | ---------------- | ------------------- | ----------------- | ---------- | ---------- | ---------- | ----------- | -------------------------------- |
| ELD001     | Beginner ELD     | K-2                 | Spanish, Mandarin | 2021-08-15 | 2022-06-15 | 25         | Ms. Johnson | Picture Books, Role-Play         |
| ELD002     | Intermediate ELD | 3-5                 | Spanish, Arabic   | 2021-08-15 | 2022-06-15 | 20         | Mr. Lee     | Short Stories, Group Discussions |


### `**data/student_engagement.csv**`


| student_id | program_id | engagement_score | language_progress | storytelling_participation | assessment_scores | feedback                       |
| ---------- | ---------- | ---------------- | ----------------- | -------------------------- | ----------------- | ------------------------------ |
| STU001     | ELD001     | 4.5              | Advanced          | High                       | 85                | Enjoys storytelling activities |
| STU002     | ELD001     | 3.8              | Intermediate      | Medium                     | 78                | Needs more support in speaking |


### `**data/storytelling_strategies.csv**`


| strategy_id | strategy_name | target_skills         | effectiveness_score | implementation_cost | suitable_grade_levels |
| ----------- | ------------- | --------------------- | ------------------- | ------------------- | --------------------- |
| STR001      | Picture Books | Vocabulary, Listening | 4.5                 | Low                 | K-2                   |
| STR002      | Role-Play     | Speaking, Confidence  | 4.8                 | Medium              | K-5                   |


### `**data/learning_outcomes.csv**`


| outcome_id | program_id | student_id | pre_assessment_score | post_assessment_score | language_growth | storytelling_impact | semester  |
| ---------- | ---------- | ---------- | -------------------- | --------------------- | --------------- | ------------------- | --------- |
| OUT001     | ELD001     | STU001     | 60                   | 85                    | Significant     | High                | Fall 2021 |
| OUT002     | ELD001     | STU002     | 55                   | 78                    | Moderate        | Medium              | Fall 2021 |


---

##  **Use Cases**


| **Scenario**                       | **Module**                      | **What It Does**                                                                  | **Example Output**                                                         |
| ---------------------------------- | ------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Design a new ELD program           | ELD Program Designer            | Creates a program with grade levels, language focus, and storytelling strategies. | `{"program_id": "ELD004", "program_name": "Advanced ELD for High School"}` |
| Analyze student engagement         | Student Engagement Tracker      | Calculates avg. engagement score and identifies at-risk students.                 | `{"avg_engagement_score": "4.20", "at_risk_students": 2}`                  |
| Recommend storytelling strategies  | Storytelling Strategy Optimizer | Suggests strategies based on target skills, grade level, and budget.              | `[{"strategy_name": "Role-Play", "effectiveness_score": 4.8}]`             |
| Correlate strategies with outcomes | Learning Outcome Analyzer       | Links storytelling strategies to student growth and assessment scores.            | `{"avg_growth": "18.50", "storytelling_impact_distribution": {"High": 3}}` |


---

##  **Customization**

### **1. Replace Sample Data**

Replace the **sample CSV files** in the `data/` directory with your **real ELD program data** for accurate insights.

### **2. Extend Functionality**

- **Integrate with School Systems**: Connect to **student information systems (SIS)** or **learning management systems (LMS)** for live data.
- **Add Machine Learning**: Use `scikit-learn` to **predict student success** based on engagement and outcome data.
- **Automate Reports**: Use `smtplib` to **email reports** to educators and administrators.

### **3. Add a Dashboard (Optional)**

Use **Streamlit** to create a live dashboard for visualizing:

- **ELD program enrollment** and details.
- **Student engagement trends** (scores, progress).
- **Storytelling strategy effectiveness**.
- **Learning outcome correlations**.

**Example Dashboard Code (`dashboard.py`):**

```python
# Install Streamlit: pip install streamlit
import streamlit as st
import pandas as pd

st.title("🎓 ELD Program Dashboard")

# Load data
programs_df = pd.read_csv("data/eld_programs.csv")
engagement_df = pd.read_csv("data/student_engagement.csv")

# Visualize program enrollment
st.subheader("📚 ELD Program Enrollment")
st.bar_chart(programs_df, x="program_name", y="enrollment")

# Visualize engagement scores
st.subheader("📊 Student Engagement Scores")
st.line_chart(engagement_df, x="student_id", y="engagement_score")
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

### **4. Scale for Your District**

- Add **more programs** to `eld_programs.csv` (e.g., for different schools or grade levels).
- Track **additional metrics** (e.g., attendance, parent engagement).
- Extend the **Storytelling Strategy Optimizer** to include **cultural relevance** or **technology integration**.

---

##  **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details. You are free to use, modify, and distribute this toolkit for any purpose.
