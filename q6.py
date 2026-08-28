import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/processed_student_performance.csv")

plt.figure(figsize=(80, 10))
plt.grid(True, linestyle='--', axis='y')
plt.bar(df['Student'], df['Final_Score'], linewidth=10)
plt.xlabel('Student Names', fontsize=30)
plt.xticks(fontsize=10)
plt.ylabel('Final Scores', fontsize=30)
plt.title('Final Scores of Students', fontsize=50)
plt.savefig('plots/final_scores.png')
plt.close

plt.figure(figsize=(10, 6))
plt.scatter(df['Hours_Studied'], df['Final_Score'])
plt.xlabel('Hours Studied', fontsize=10)
plt.ylabel('Final Scores', fontsize=10)
plt.title('Relationship btw Hours Studied & Final Scores', fontsize=30)
plt.grid(True, linestyle='--')
plt.savefig('plots/study_vs_score.png')
plt.close()

plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(df['Final_Score'], bins=30, edgecolor='black')
plt.bar_label(patches, padding= 5, fontsize=8)
plt.xlabel('Final Scores', fontsize=10)
plt.ylabel('Frequency', fontsize=10)
plt.title('Distribution of Final Scores', fontsize=30)
plt.grid(True, linestyle='--')
plt.savefig('plots/score_distribution.png')
plt.close()

plt.figure(figsize=(10, 6))
plt.bar(df['Attendance'], -df['Improvement'], linewidth=10)
plt.xlabel('Attendance', fontsize=10)
plt.ylabel('Deterioration', fontsize=10)
plt.title('Relationship btw Attendance & Deterioration', fontsize=30)
plt.grid(True, linestyle='--')
plt.savefig('plots/attendance_vs_deterioration.png')
plt.close()