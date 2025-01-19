Hey folks , I am  excited to announce something about my project of building a "DIABETES PREDICTION MODEL " with comparison of four different algorithms and finding out the best one which predicts it more accurately . 

  The  utilized algorithms are 

 1) Logistic regression 

 2) Support Vector Machines

 3) Decision Trees

 4) Random Forest Classifier.

💡 Mainly Utilized Evaluation Metrics are :

 1) Accuracy :

        It discusses about how accurately a model predicts 

       FORMULA = no of  correct predictions / total  no of predictions 

EXAMPLE: If 90 persons are correctly predicted then accuracy will be 90%

2) Precision:

         It says how many of the predicted positives are actually correct 

      FORMULA =TP/TP+FP 

      HERE  TP => True positives , FP => False Positives 

    EXAMPLE : If doctor says  90 persons are diabetic then how many of them are actually diabetic within that predicted ones . For case if we assume only 50 are actually diabetic within that 90 then precision can given as 55%

3) Recall : 

            It predicts how many  positives  are identified out of all positives

    FORMULA : TP/TP+FN 

         FN=>false negative 

    EXAMPLE : Out of  90 affected persons  if you find 20 then recall will be 20/90 = 22%

  

⭕ Now there may be some sort of confusion between the recall and precision so for simple case precision focuses on the idea of avoiding false positives .

 whereas recall focuses on the idea of ignoring false negatives

4) F1 score:

       It provides a trade-off between recall and precision 

   FORMULA : 2* (P * R )/ (P+R)

   5) Confusion matrix:

       It actually gives a tabular form where there are two rows and two columns and they  consists of four terms 

    1) True positive : it correctly identifies what is actually true  

    2) True Negative : it correctly predicts negative 

    3) False Positive : it predicts  output as  positive but actually it is negative 

    4) True  Negative : it predicts output as negative but actually it is positive 

✅ so after analysing all these parameters for the listeed four algorithms l found that "Random forest " Performs well 

🔷 Evaluation metrics using RFC

💠 accuracy : 0.7662337662337663

💠 precision : 0.6666666666666666

💠 recall : 0.65

💠 f1_score : 0.6582278481012658

💠 confusion_matrix : [[125 26]

                               [ 28 52]]

so my further idea is of deploying it as an ui with help of streamlit and l am exploring about it .

 check out my github for source code :



watch a small video of my work and provide your feedback 
