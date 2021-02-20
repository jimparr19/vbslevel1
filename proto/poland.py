from pypbl.elicitation import BayesPreference
from pypbl.priors import Normal

from config import beer_features_df, beer_features_min, beer_features_max, features

normalised_available_beers_df = (beer_features_df - beer_features_min) / (
        beer_features_max - beer_features_min)

model = BayesPreference(data=normalised_available_beers_df, normalise=False)
model.set_priors([Normal() for _ in features])

preference_data = [
    ['Surfer', 'Kviek Session IPA'],
    ['Pierwsza Pomoc', 'Surfer'],
    ['American Beauty', 'Pierwsza Pomoc'],
    ['Pan Ipani Double', 'American Beauty'],
    ['Pan Ipani Double', 'Hazy Morning'],
    ['Pan Ipani Double', 'Piece of Cake']
]

for preference in preference_data:
    model.add_strict_preference(preference[0], preference[1])

model.infer_weights()

beer_features_df['utility'] = [model.weights.dot(row.values) for i, row in normalised_available_beers_df.iterrows()]
rank_df = beer_features_df.sort_values(by='utility', ascending=False)

print(rank_df)
print(list(zip(features, model.weights)))
print('end')
