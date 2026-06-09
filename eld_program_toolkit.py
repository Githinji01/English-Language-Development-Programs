import pandas as pd
import numpy as np
import os
import json
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional, Union

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('eld_program.log'), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# ======================
# 1. ELD PROGRAM DESIGNER
# ======================
class ELDProgramDesigner:
    """Designs and manages ELD programs for multilingual learners."""

    def __init__(self, programs_data_path: str = "data/eld_programs.csv"):
        self.programs_data_path = programs_data_path
        self.programs = self._load_programs_data()

    def _load_programs_data(self) -> pd.DataFrame:
        """Load or create sample ELD program data."""
        if not os.path.exists(self.programs_data_path):
            sample_data = {
                "program_id": ["ELD001", "ELD002", "ELD003"],
                "program_name": ["Beginner ELD", "Intermediate ELD", "Advanced ELD"],
                "target_grade_levels": ["K-2", "3-5", "6-8"],
                "language_focus": ["Spanish, Mandarin", "Spanish, Arabic", "Mandarin, Vietnamese"],
                "start_date": ["2021-08-15", "2021-08-15", "2021-08-15"],
                "end_date": ["2022-06-15", "2022-06-15", "2022-06-15"],
                "enrollment": [25, 20, 15],
                "instructors": ["Ms. Johnson", "Mr. Lee", "Ms. Garcia"],
                "storytelling_strategies": ["Picture Books, Role-Play", "Short Stories, Group Discussions", "Novels, Debates"]
            }
            pd.DataFrame(sample_data).to_csv(self.programs_data_path, index=False)
            logger.info(f"Created sample ELD programs data at {self.programs_data_path}")
        return pd.read_csv(self.programs_data_path)

    def design_program(self, program_name: str, target_grade_levels: str, language_focus: str,
                       start_date: str, end_date: str, instructors: str, storytelling_strategies: str) -> Dict:
        """Design a new ELD program."""
        new_program = pd.DataFrame([{
            "program_id": f"ELD{len(self.programs) + 1:03d}",
            "program_name": program_name,
            "target_grade_levels": target_grade_levels,
            "language_focus": language_focus,
            "start_date": start_date,
            "end_date": end_date,
            "enrollment": 0,  # Initialize with 0 enrollment
            "instructors": instructors,
            "storytelling_strategies": storytelling_strategies
        }])
        self.programs = pd.concat([self.programs, new_program], ignore_index=True)
        self.programs.to_csv(self.programs_data_path, index=False)
        logger.info(f"Designed new ELD program: {program_name}")
        return {
            "status": "Success",
            "program_id": new_program["program_id"].iloc[0],
            "program_name": program_name,
            "message": f"ELD program '{program_name}' designed successfully."
        }

    def update_enrollment(self, program_id: str, new_enrollment: int) -> Dict:
        """Update the enrollment count for an ELD program."""
        program = self.programs[self.programs["program_id"] == program_id]
        if program.empty:
            logger.error(f"Program {program_id} not found.")
            return {"error": f"Program {program_id} not found."}

        self.programs.loc[self.programs["program_id"] == program_id, "enrollment"] = new_enrollment
        self.programs.to_csv(self.programs_data_path, index=False)
        logger.info(f"Updated enrollment for {program_id} to {new_enrollment}")
        return {
            "status": "Success",
            "program_id": program_id,
            "new_enrollment": new_enrollment,
            "message": f"Enrollment for {program_id} updated to {new_enrollment}."
        }

    def get_program_details(self, program_id: str) -> Dict:
        """Retrieve details of a specific ELD program."""
        program = self.programs[self.programs["program_id"] == program_id]
        if program.empty:
            logger.error(f"Program {program_id} not found.")
            return {"error": f"Program {program_id} not found."}
        return program.iloc[0].to_dict()

    def generate_program_report(self, output_file: str = "reports/eld_program_report.md") -> str:
        """Generate a Markdown report of all ELD programs."""
        os.makedirs("reports", exist_ok=True)
        report = f"# ELD Program Report\n\n"
        report += f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        report += "## ELD Programs Overview\n"
        report += f"- **Total Programs:** {len(self.programs)}\n"
        report += f"- **Total Enrollment:** {self.programs['enrollment'].sum()}\n\n"

        report += "## Program Details\n"
        for _, program in self.programs.iterrows():
            report += f"\n### {program['program_name']} ({program['program_id']})\n"
            report += f"- **Target Grade Levels:** {program['target_grade_levels']}\n"
            report += f"- **Language Focus:** {program['language_focus']}\n"
            report += f"- **Duration:** {program['start_date']} to {program['end_date']}\n"
            report += f"- **Enrollment:** {program['enrollment']}\n"
            report += f"- **Instructors:** {program['instructors']}\n"
            report += f"- **Storytelling Strategies:** {program['storytelling_strategies']}\n"

        with open(output_file, "w") as f:
            f.write(report)
        logger.info(f"Generated ELD program report at {output_file}")
        return report

# ======================
# 2. STUDENT ENGAGEMENT TRACKER
# ======================
class StudentEngagementTracker:
    """Tracks student engagement and learning outcomes for ELD programs."""

    def __init__(self, engagement_data_path: str = "data/student_engagement.csv"):
        self.engagement_data_path = engagement_data_path
        self.engagement = self._load_engagement_data()

    def _load_engagement_data(self) -> pd.DataFrame:
        """Load or create sample student engagement data."""
        if not os.path.exists(self.engagement_data_path):
            sample_data = {
                "student_id": ["STU001", "STU002", "STU003", "STU004"],
                "program_id": ["ELD001", "ELD001", "ELD002", "ELD003"],
                "engagement_score": [4.5, 3.8, 4.2, 4.9],
                "language_progress": ["Advanced", "Intermediate", "Advanced", "Beginner"],
                "storytelling_participation": ["High", "Medium", "High", "High"],
                "assessment_scores": [85, 78, 90, 95],
                "feedback": ["Enjoys storytelling activities", "Needs more support in speaking", "Excellent progress", "Very engaged"]
            }
            pd.DataFrame(sample_data).to_csv(self.engagement_data_path, index=False)
            logger.info(f"Created sample student engagement data at {self.engagement_data_path}")
        return pd.read_csv(self.engagement_data_path)

    def log_engagement(self, student_id: str, program_id: str, engagement_score: float,
                       language_progress: str, storytelling_participation: str,
                       assessment_score: int, feedback: str) -> Dict:
        """Log student engagement and learning outcomes."""
        new_engagement = pd.DataFrame([{
            "student_id": student_id,
            "program_id": program_id,
            "engagement_score": engagement_score,
            "language_progress": language_progress,
            "storytelling_participation": storytelling_participation,
            "assessment_scores": assessment_score,
            "feedback": feedback
        }])
        self.engagement = pd.concat([self.engagement, new_engagement], ignore_index=True)
        self.engagement.to_csv(self.engagement_data_path, index=False)
        logger.info(f"Logged engagement for student {student_id} in program {program_id}")
        return {
            "status": "Success",
            "student_id": student_id,
            "program_id": program_id,
            "engagement_score": engagement_score,
            "message": f"Engagement logged for {student_id}."
        }

    def analyze_engagement(self, program_id: Optional[str] = None) -> Dict:
        """Analyze student engagement for a specific program or all programs."""
        if program_id:
            engagement_data = self.engagement[self.engagement["program_id"] == program_id]
            if engagement_data.empty:
                logger.error(f"No engagement data found for program {program_id}.")
                return {"error": f"No engagement data found for program {program_id}."}
        else:
            engagement_data = self.engagement

        analysis = {
            "total_students": len(engagement_data),
            "avg_engagement_score": f"{engagement_data['engagement_score'].mean():.2f}",
            "avg_assessment_score": f"{engagement_data['assessment_scores'].mean():.2f}",
            "language_progress_distribution": engagement_data["language_progress"].value_counts().to_dict(),
            "storytelling_participation_distribution": engagement_data["storytelling_participation"].value_counts().to_dict(),
            "students": []
        }

        for _, student in engagement_data.iterrows():
            analysis["students"].append({
                "student_id": student["student_id"],
                "engagement_score": student["engagement_score"],
                "language_progress": student["language_progress"],
                "storytelling_participation": student["storytelling_participation"],
                "assessment_score": student["assessment_scores"],
                "feedback": student["feedback"]
            })

        logger.info(f"Analyzed engagement for {'all programs' if not program_id else program_id}")
        return analysis

    def identify_at_risk_students(self, threshold_score: float = 4.0) -> List[Dict]:
        """Identify students at risk based on engagement and assessment scores."""
        at_risk_students = []
        for _, student in self.engagement.iterrows():
            if student["engagement_score"] < threshold_score or student["assessment_scores"] < 70:
                at_risk_students.append({
                    "student_id": student["student_id"],
                    "program_id": student["program_id"],
                    "engagement_score": student["engagement_score"],
                    "assessment_score": student["assessment_scores"],
                    "language_progress": student["language_progress"],
                    "risk_reason": "Low engagement" if student["engagement_score"] < threshold_score
                    else "Low assessment score"
                })
        logger.info(f"Identified {len(at_risk_students)} at-risk students")
        return at_risk_students

    def generate_engagement_report(self, output_file: str = "reports/student_engagement_report.md") -> str:
        """Generate a Markdown report of student engagement and outcomes."""
        os.makedirs("reports", exist_ok=True)
        report = f"# Student Engagement Report\n\n"
        report += f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        analysis = self.analyze_engagement()
        report += "## Engagement Overview\n"
        report += f"- **Total Students:** {analysis['total_students']}\n"
        report += f"- **Average Engagement Score:** {analysis['avg_engagement_score']}\n"
        report += f"- **Average Assessment Score:** {analysis['avg_assessment_score']}\n\n"

        report += "## Language Progress Distribution\n"
        for progress, count in analysis["language_progress_distribution"].items():
            report += f"- **{progress}:** {count} students\n"

        report += "\n## Storytelling Participation Distribution\n"
        for participation, count in analysis["storytelling_participation_distribution"].items():
            report += f"- **{participation}:** {count} students\n"

        at_risk_students = self.identify_at_risk_students()
        report += f"\n## At-Risk Students ({len(at_risk_students)})\n"
        if at_risk_students:
            for student in at_risk_students:
                report += f"\n### Student {student['student_id']} (Program: {student['program_id']})\n"
                report += f"- **Engagement Score:** {student['engagement_score']}\n"
                report += f"- **Assessment Score:** {student['assessment_score']}\n"
                report += f"- **Language Progress:** {student['language_progress']}\n"
                report += f"- **Risk Reason:** {student['risk_reason']}\n"
        else:
            report += "\nNo at-risk students identified."

        with open(output_file, "w") as f:
            f.write(report)
        logger.info(f"Generated student engagement report at {output_file}")
        return report

# ======================
# 3. STORYTELLING STRATEGY OPTIMIZER
# ======================
class StorytellingStrategyOptimizer:
    """Optimizes storytelling-based instructional strategies for ELD programs."""

    def __init__(self, strategies_data_path: str = "data/storytelling_strategies.csv"):
        self.strategies_data_path = strategies_data_path
        self.strategies = self._load_strategies_data()

    def _load_strategies_data(self) -> pd.DataFrame:
        """Load or create sample storytelling strategies data."""
        if not os.path.exists(self.strategies_data_path):
            sample_data = {
                "strategy_id": ["STR001", "STR002", "STR003", "STR004"],
                "strategy_name": ["Picture Books", "Role-Play", "Short Stories", "Group Discussions"],
                "target_skills": ["Vocabulary, Listening", "Speaking, Confidence", "Reading, Comprehension", "Speaking, Collaboration"],
                "effectiveness_score": [4.5, 4.8, 4.2, 4.6],
                "implementation_cost": ["Low", "Medium", "Low", "Low"],
                "suitable_grade_levels": ["K-2", "K-5", "3-8", "3-8"]
            }
            pd.DataFrame(sample_data).to_csv(self.strategies_data_path, index=False)
            logger.info(f"Created sample storytelling strategies data at {self.strategies_data_path}")
        return pd.read_csv(self.strategies_data_path)

    def add_strategy(self, strategy_name: str, target_skills: str, implementation_cost: str,
                    suitable_grade_levels: str) -> Dict:
        """Add a new storytelling strategy."""
        new_strategy = pd.DataFrame([{
            "strategy_id": f"STR{len(self.strategies) + 1:03d}",
            "strategy_name": strategy_name,
            "target_skills": target_skills,
            "effectiveness_score": 0.0,  # Initialize with 0, to be updated later
            "implementation_cost": implementation_cost,
            "suitable_grade_levels": suitable_grade_levels
        }])
        self.strategies = pd.concat([self.strategies, new_strategy], ignore_index=True)
        self.strategies.to_csv(self.strategies_data_path, index=False)
        logger.info(f"Added new storytelling strategy: {strategy_name}")
        return {
            "status": "Success",
            "strategy_id": new_strategy["strategy_id"].iloc[0],
            "strategy_name": strategy_name,
            "message": f"Storytelling strategy '{strategy_name}' added successfully."
        }

    def update_effectiveness(self, strategy_id: str, new_score: float) -> Dict:
        """Update the effectiveness score of a storytelling strategy."""
        strategy = self.strategies[self.strategies["strategy_id"] == strategy_id]
        if strategy.empty:
            logger.error(f"Strategy {strategy_id} not found.")
            return {"error": f"Strategy {strategy_id} not found."}

        self.strategies.loc[self.strategies["strategy_id"] == strategy_id, "effectiveness_score"] = new_score
        self.strategies.to_csv(self.strategies_data_path, index=False)
        logger.info(f"Updated effectiveness score for {strategy_id} to {new_score}")
        return {
            "status": "Success",
            "strategy_id": strategy_id,
            "new_score": new_score,
            "message": f"Effectiveness score for {strategy_id} updated to {new_score}."
        }

    def recommend_strategies(self, target_skills: List[str], grade_level: str, budget: str = "Low") -> List[Dict]:
        """Recommend storytelling strategies based on target skills, grade level, and budget."""
        recommendations = []
        for _, strategy in self.strategies.iterrows():
            skills_match = all(skill in strategy["target_skills"].split(", ") for skill in target_skills)
            grade_match = grade_level in strategy["suitable_grade_levels"].split(", ")
            budget_match = strategy["implementation_cost"] == budget or budget == "Any"

            if skills_match and grade_match and budget_match:
                recommendations.append({
                    "strategy_id": strategy["strategy_id"],
                    "strategy_name": strategy["strategy_name"],
                    "target_skills": strategy["target_skills"],
                    "effectiveness_score": strategy["effectiveness_score"],
                    "implementation_cost": strategy["implementation_cost"],
                    "suitable_grade_levels": strategy["suitable_grade_levels"]
                })

        # Sort by effectiveness score (descending)
        recommendations.sort(key=lambda x: x["effectiveness_score"], reverse=True)
        logger.info(f"Recommended {len(recommendations)} strategies for {target_skills}, {grade_level}, {budget}")
        return recommendations

    def generate_strategy_report(self, output_file: str = "reports/storytelling_strategy_report.md") -> str:
        """Generate a Markdown report of storytelling strategies."""
        os.makedirs("reports", exist_ok=True)
        report = f"# Storytelling Strategy Report\n\n"
        report += f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        report += "## Strategy Overview\n"
        report += f"- **Total Strategies:** {len(self.strategies)}\n"
        report += f"- **Average Effectiveness Score:** {self.strategies['effectiveness_score'].mean():.2f}\n\n"

        report += "## Strategy Details\n"
        for _, strategy in self.strategies.iterrows():
            report += f"\n### {strategy['strategy_name']} ({strategy['strategy_id']})\n"
            report += f"- **Target Skills:** {strategy['target_skills']}\n"
            report += f"- **Effectiveness Score:** {strategy['effectiveness_score']}\n"
            report += f"- **Implementation Cost:** {strategy['implementation_cost']}\n"
            report += f"- **Suitable Grade Levels:** {strategy['suitable_grade_levels']}\n"

        with open(output_file, "w") as f:
            f.write(report)
        logger.info(f"Generated storytelling strategy report at {output_file}")
        return report

# ======================
# 4. LEARNING OUTCOME ANALYZER
# ======================
class LearningOutcomeAnalyzer:
    """Analyzes learning outcomes and correlates them with ELD programs and storytelling strategies."""

    def __init__(self, outcomes_data_path: str = "data/learning_outcomes.csv"):
        self.outcomes_data_path = outcomes_data_path
        self.outcomes = self._load_outcomes_data()

    def _load_outcomes_data(self) -> pd.DataFrame:
        """Load or create sample learning outcomes data."""
        if not os.path.exists(self.outcomes_data_path):
            sample_data = {
                "outcome_id": ["OUT001", "OUT002", "OUT003", "OUT004"],
                "program_id": ["ELD001", "ELD001", "ELD002", "ELD003"],
                "student_id": ["STU001", "STU002", "STU003", "STU004"],
                "pre_assessment_score": [60, 55, 70, 65],
                "post_assessment_score": [85, 78, 90, 95],
                "language_growth": ["Significant", "Moderate", "Significant", "Significant"],
                "storytelling_impact": ["High", "Medium", "High", "High"],
                "semester": ["Fall 2021", "Fall 2021", "Spring 2022", "Spring 2022"]
            }
            pd.DataFrame(sample_data).to_csv(self.outcomes_data_path, index=False)
            logger.info(f"Created sample learning outcomes data at {self.outcomes_data_path}")
        return pd.read_csv(self.outcomes_data_path)

    def log_outcome(self, program_id: str, student_id: str, pre_score: int, post_score: int,
                    language_growth: str, storytelling_impact: str, semester: str) -> Dict:
        """Log a student's learning outcome."""
        growth = "Significant" if (post_score - pre_score) >= 20 else "Moderate" if (post_score - pre_score) >= 10 else "Minimal"
        new_outcome = pd.DataFrame([{
            "outcome_id": f"OUT{len(self.outcomes) + 1:03d}",
            "program_id": program_id,
            "student_id": student_id,
            "pre_assessment_score": pre_score,
            "post_assessment_score": post_score,
            "language_growth": growth,
            "storytelling_impact": storytelling_impact,
            "semester": semester
        }])
        self.outcomes = pd.concat([self.outcomes, new_outcome], ignore_index=True)
        self.outcomes.to_csv(self.outcomes_data_path, index=False)
        logger.info(f"Logged learning outcome for {student_id} in {program_id}")
        return {
            "status": "Success",
            "outcome_id": new_outcome["outcome_id"].iloc[0],
            "student_id": student_id,
            "program_id": program_id,
            "language_growth": growth,
            "message": f"Learning outcome logged for {student_id}."
        }

    def analyze_outcomes(self, program_id: Optional[str] = None) -> Dict:
        """Analyze learning outcomes for a specific program or all programs."""
        if program_id:
            outcomes_data = self.outcomes[self.outcomes["program_id"] == program_id]
            if outcomes_data.empty:
                logger.error(f"No outcomes data found for program {program_id}.")
                return {"error": f"No outcomes data found for program {program_id}."}
        else:
            outcomes_data = self.outcomes

        analysis = {
            "total_outcomes": len(outcomes_data),
            "avg_pre_score": f"{outcomes_data['pre_assessment_score'].mean():.2f}",
            "avg_post_score": f"{outcomes_data['post_assessment_score'].mean():.2f}",
            "avg_growth": f"{(outcomes_data['post_assessment_score'] - outcomes_data['pre_assessment_score']).mean():.2f}",
            "language_growth_distribution": outcomes_data["language_growth"].value_counts().to_dict(),
            "storytelling_impact_distribution": outcomes_data["storytelling_impact"].value_counts().to_dict(),
            "outcomes": []
        }

        for _, outcome in outcomes_data.iterrows():
            analysis["outcomes"].append({
                "outcome_id": outcome["outcome_id"],
                "student_id": outcome["student_id"],
                "pre_score": outcome["pre_assessment_score"],
                "post_score": outcome["post_assessment_score"],
                "growth": outcome["language_growth"],
                "storytelling_impact": outcome["storytelling_impact"],
                "semester": outcome["semester"]
            })

        logger.info(f"Analyzed outcomes for {'all programs' if not program_id else program_id}")
        return analysis

    def correlate_strategies_with_outcomes(self, program_id: str) -> Dict:
        """Correlate storytelling strategies with learning outcomes for a program."""
        program_outcomes = self.outcomes[self.outcomes["program_id"] == program_id]
        if program_outcomes.empty:
            logger.error(f"No outcomes data found for program {program_id}.")
            return {"error": f"No outcomes data found for program {program_id}."}

        # Get the storytelling strategies for the program
        eld_program = ELDProgramDesigner()
        program = eld_program.get_program_details(program_id)
        if "error" in program:
            return program

        strategies = program["storytelling_strategies"].split(", ")

        correlation = {
            "program_id": program_id,
            "program_name": program["program_name"],
            "storytelling_strategies": strategies,
            "avg_pre_score": f"{program_outcomes['pre_assessment_score'].mean():.2f}",
            "avg_post_score": f"{program_outcomes['post_assessment_score'].mean():.2f}",
            "avg_growth": f"{(program_outcomes['post_assessment_score'] - program_outcomes['pre_assessment_score']).mean():.2f}",
            "storytelling_impact_distribution": program_outcomes["storytelling_impact"].value_counts().to_dict()
        }

        logger.info(f"Correlated strategies with outcomes for {program_id}")
        return correlation

    def generate_outcomes_report(self, output_file: str = "reports/learning_outcomes_report.md") -> str:
        """Generate a Markdown report of learning outcomes."""
        os.makedirs("reports", exist_ok=True)
        report = f"# Learning Outcomes Report\n\n"
        report += f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

        analysis = self.analyze_outcomes()
        report += "## Outcomes Overview\n"
        report += f"- **Total Outcomes:** {analysis['total_outcomes']}\n"
        report += f"- **Average Pre-Assessment Score:** {analysis['avg_pre_score']}\n"
        report += f"- **Average Post-Assessment Score:** {analysis['avg_post_score']}\n"
        report += f"- **Average Growth:** {analysis['avg_growth']}\n\n"

        report += "## Language Growth Distribution\n"
        for growth, count in analysis["language_growth_distribution"].items():
            report += f"- **{growth}:** {count} students\n"

        report += "\n## Storytelling Impact Distribution\n"
        for impact, count in analysis["storytelling_impact_distribution"].items():
            report += f"- **{impact}:** {count} students\n"

        with open(output_file, "w") as f:
            f.write(report)
        logger.info(f"Generated learning outcomes report at {output_file}")
        return report

# ======================
# MAIN EXECUTION
# ======================
def main():
    print("🎓 **Mt. Diablo Unified ELD Program Toolkit**\n")
    print("Automate ELD Program Design, Student Engagement, and Learning Outcomes\n")
    print("=" * 80)

    print("\nSelect a module to run:")
    print("1. 📚 ELD Program Designer")
    print("2. 📊 Student Engagement Tracker")
    print("3. 🎭 Storytelling Strategy Optimizer")
    print("4. 📈 Learning Outcome Analyzer")
    print("5. 📄 Generate All Reports")
    print("6. 🏃 Run All Modules (Demo)\n")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # ELD Program Designer Demo
        print("\n📚 **ELD PROGRAM DESIGNER**\n")
        designer = ELDProgramDesigner()
        program = designer.get_program_details("ELD001")
        print("📋 Program Details for ELD001:")
        print(json.dumps(program, indent=2))

        new_program = designer.design_program(
            program_name="Advanced ELD for High School",
            target_grade_levels="9-12",
            language_focus="Spanish, Arabic, Vietnamese",
            start_date="2022-08-15",
            end_date="2023-06-15",
            instructors="Ms. Smith",
            storytelling_strategies="Debates, Presentations, Novel Studies"
        )
        print("\n✅ New Program Designed:")
        print(json.dumps(new_program, indent=2))

        report = designer.generate_program_report()
        print(f"\n📄 ELD program report generated at: reports/eld_program_report.md")

    elif choice == "2":
        # Student Engagement Tracker Demo
        print("\n📊 **STUDENT ENGAGEMENT TRACKER**\n")
        tracker = StudentEngagementTracker()
        engagement = tracker.analyze_engagement("ELD001")
        print("📈 Engagement Analysis for ELD001:")
        print(json.dumps(engagement, indent=2))

        at_risk = tracker.identify_at_risk_students()
        print("\n⚠️  At-Risk Students:")
        for student in at_risk:
            print(f"   - {student['student_id']}: {student['risk_reason']}")

        report = tracker.generate_engagement_report()
        print(f"\n📄 Student engagement report generated at: reports/student_engagement_report.md")

    elif choice == "3":
        # Storytelling Strategy Optimizer Demo
        print("\n🎭 **STORYTELLING STRATEGY OPTIMIZER**\n")
        optimizer = StorytellingStrategyOptimizer()
        recommendations = optimizer.recommend_strategies(
            target_skills=["Speaking", "Confidence"],
            grade_level="K-5",
            budget="Low"
        )
        print("💡 Recommended Strategies:")
        for strategy in recommendations:
            print(f"   - {strategy['strategy_name']} (Effectiveness: {strategy['effectiveness_score']})")

        report = optimizer.generate_strategy_report()
        print(f"\n📄 Storytelling strategy report generated at: reports/storytelling_strategy_report.md")

    elif choice == "4":
        # Learning Outcome Analyzer Demo
        print("\n📈 **LEARNING OUTCOME ANALYZER**\n")
        analyzer = LearningOutcomeAnalyzer()
        outcomes = analyzer.analyze_outcomes("ELD001")
        print("📊 Learning Outcomes for ELD001:")
        print(json.dumps(outcomes, indent=2))

        correlation = analyzer.correlate_strategies_with_outcomes("ELD001")
        print("\n🔗 Strategy-Outcome Correlation for ELD001:")
        print(json.dumps(correlation, indent=2))

        report = analyzer.generate_outcomes_report()
        print(f"\n📄 Learning outcomes report generated at: reports/learning_outcomes_report.md")

    elif choice == "5":
        # Generate All Reports
        print("\n📄 **GENERATING ALL REPORTS**\n")
        designer = ELDProgramDesigner()
        tracker = StudentEngagementTracker()
        optimizer = StorytellingStrategyOptimizer()
        analyzer = LearningOutcomeAnalyzer()

        designer.generate_program_report()
        tracker.generate_engagement_report()
        optimizer.generate_strategy_report()
        analyzer.generate_outcomes_report()

        print("✅ All reports generated in the 'reports/' directory.")

    elif choice == "6":
        # Run All Modules
        print("\n🏃 **RUNNING ALL MODULES (DEMO)**\n")
        print("=" * 80)

        # ELD Program Designer
        print("\n📚 **ELD PROGRAM DESIGNER**")
        designer = ELDProgramDesigner()
        programs = designer.programs
        print(f"Total ELD Programs: {len(programs)}")
        print(f"Total Enrollment: {programs['enrollment'].sum()}")

        # Student Engagement Tracker
        print("\n📊 **STUDENT ENGAGEMENT TRACKER**")
        tracker = StudentEngagementTracker()
        engagement = tracker.analyze_engagement()
        print(f"Total Students: {engagement['total_students']}")
        print(f"Average Engagement Score: {engagement['avg_engagement_score']}")

        # Storytelling Strategy Optimizer
        print("\n🎭 **STORYTELLING STRATEGY OPTIMIZER**")
        optimizer = StorytellingStrategyOptimizer()
        strategies = optimizer.strategies
        print(f"Total Strategies: {len(strategies)}")
        print(f"Average Effectiveness Score: {strategies['effectiveness_score'].mean():.2f}")

        # Learning Outcome Analyzer
        print("\n📈 **LEARNING OUTCOME ANALYZER**")
        analyzer = LearningOutcomeAnalyzer()
        outcomes = analyzer.analyze_outcomes()
        print(f"Total Outcomes: {outcomes['total_outcomes']}")
        print(f"Average Growth: {outcomes['avg_growth']}")

        print("\n" + "=" * 80)
        print("✅ All modules executed successfully!")

    else:
        print("❌ Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    # Create data and reports directories if they don't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("reports"):
        os.makedirs("reports")
    main()
