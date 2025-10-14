from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

X = ["buy cheap meds", "win cash now", "hello friend", "meeting at noon"]
y = [1, 1, 0, 0]  # 1 = Spam, 0 = Not Spam

vec = CountVectorizer()
X_vec = vec.fit_transform(X)

model = MultinomialNB()
model.fit(X_vec, y)

test = vec.transform(["hello friend win cheap meds"])
# print(model.predict(test))  # Output: [1] (Spam)

if model.predict(test) == 1:
    print("Spam")
else:
    print("Not Spam")



print('Thanks For Using Our Service 😚')

