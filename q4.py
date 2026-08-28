import numpy as np

Hours_studied = np.array([5.9, 3.6, 6.5, 5.4, 1.2, 7.3])
Attendance = np.array([100, 85, 73, 73, 74, 92])
Previous_Score = np.array([52, 74, 49, 85, 78, 77])
Final_Score = np.array([60, 47, 41, 75, 35, 69])

print(np.shape(Hours_studied))
print(np.shape(Attendance))
print(np.shape(Previous_Score))
print(np.shape(Final_Score))

print(Hours_studied.dtype)
print(Attendance.dtype)
print(Previous_Score.dtype)
print(Final_Score.dtype)

avg =round(np.mean(Final_Score), 2)
print(avg)
print(np.max(Final_Score))
print(np.min(Final_Score))
std_dev= round(np.std(Final_Score), 2)
print(std_dev)
print(Final_Score+5)
marks = Final_Score >= 75
print(marks)
print(Final_Score[marks])