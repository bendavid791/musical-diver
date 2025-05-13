# UFC Fight Predictor

This project builds machine learning models to predict the outcome of UFC fights based on fighter statistics. Given two fighters, it outputs the predicted probability of victory using multiple models including Logistic Regression, Random Forest, and XGBoost.

---

## Models Used

- **Logistic Regression** (baseline, interpretable and calibrated)
- **Random Forest** (ensemble of decision trees)
- **XGBoost** (gradient boosting, high performance)

Each model outputs a predicted **probability that Fighter 1 will win** the matchup.

---

## Features Used

Fighter statistics are preprocessed into differences between Fighter 1 and Fighter 2, such as:

- Wins / losses difference
- Height and reach difference
- Striking accuracy and defense
- Takedown metrics
- Age difference
- Submission attempts

## How it Works
- Fighter statistics are stored in fighter_stats.csv.
- Feature engineering computes differences between two fighters.
- Models are trained on historical fight data.
- For any matchup, predictions are made with .predict_proba() to get win probabilities.

## Example Usage
1. Run notebook to load datasets, do feature engineering, and train models
2. Get fighter stats for the matchup you want
  ``info = get_fighter_info(fighter_data, "Islam Makhachev", "Jack Della Maddalena")``
3. Compute stat differences
  ``diffs = calc_fighter_diffs(info)``
4. Predict win probabilities
  ``calc_fight_probabilities(diffs)``
