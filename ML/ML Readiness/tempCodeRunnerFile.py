new = scaler.transform([[7, 85, 9]])   # 7hrs study, 85% attend, 9 tasks 
# pred = model.predict(new)[0]
# prob = model.predict_proba(new)[0]
# print(f'Prediction: {"PASS" if pred == 1 else "FAIL"} | Probability: {prob[1]*100:.1f}%')