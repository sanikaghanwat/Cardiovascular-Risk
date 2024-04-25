In this project worked on a project using data about people's age ,habits abd health (like BMI , BP...) to predict their chance of getting heart disease in the next 10 years using Machine Learning.

Data Gathering :
Collect the data from kaggle . dataset contains 3390 rows and 17 columns.

EDA:
The study reveals a mere 15% positivity rate for CHD among patients, indicating an imbalance in the dependent variable.
Female patients are more than male patients in the study.
Nearly half of the patients are smokers.
22 patients in the study have experienced a stroke.
1069 patients have histroy of Hypertension.
About 100 patients in the study are taking blood pressure medication.
Diabetes is present in 87 patients.
Older patients face a higher risk of CHD compared to younger ones.
Male patients exhibit a significantly higher risk  of CHD compared to females .
Patients taking blood pressure medication have a significantly higher risk (33%) of CHD compared to others (14%).
Patients with a history of stroke have a significantly higher risk (45%) of CHD compared to others (14%).
Hypertensive patients have a significantly higher risk (23%) of CHD compared to others (11%).
Diabetic patients have a significantly higher risk (37%) of CHD compared to others (14%).
Systolic and diastolic blood pressure are highly correlated.

Feature Engineering and Preprocessing :
Feature selection was performed using variance inflation factor to remove multicollinearity and . 
Handling the missing value categorical column replace ny mode and numrical column replace by mean.
Detect the outliers using box plot and remove them

Handling Imbalanced Dataset: 
The distribution of the target variable, TenYearCHD, was found to be imbalanced, with only 15% of individuals classified as having a high risk of developing CHD. To address this issue, we employed the Synthetic Minority Oversampling Technique (SMOTE) to create a balanced dataset.
Model Selection and Evaluation: We split the data into train and test sets, ensuring stratified samples of both classes. We evaluated several classification models, including Logistic Regression,KNN,Decision tree, Random Forest, and SVM. Various metrics such as Precision, Recall, F1 Score, Accuracy, and AUC-ROC were compared using classification reports and confusion matrices. Considering our objective of reducing false negatives, emphasizing Recall was essential. After thorough experimentation, Decision Tree Classifier as the optimal model, achieving the highest metrics overall.

Model Deployment: Based on our evaluations and comparisons, we selected Decision Tree Classifier as our final model for deployment. demonstrated superior Recall, Precision, F1 Score, Accuracy

Conclusion:
this project presented an extensive exploration of the Cardiovascular Risk Prediction dataset, employing various machine learning techniques to predict the 10-year risk of developing coronary heart disease. By combining data processing, feature engineering, model evaluation, and selection, we successfully built an accurate model capable of identifying potential CHD patients in the future.
