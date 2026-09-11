# Assignment-4, Cognitive Computing UCS420
# Cognitive FAQ System Using Pandas
# Nilabh Kishore Gupta

import pandas as pd

roll_number = "1024170059"

# Q1. Build personalized knowledge base from last two digits of roll number
last_two = roll_number[-2:]
d1 = int(last_two[0])
d2 = int(last_two[1])
categories = ["billing", "account", "general"]
cat1 = categories[d1 % 3]
cat2 = categories[d2 % 3]

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee", "category": "billing"},
]

personal_entries = [
    {"question": "what are the college timings on saturday", "answer": "College remains open till 1 PM on Saturdays.",
     "keywords": "saturday timing college", "category": cat1},
    {"question": "how do i get a fee receipt", "answer": "You can download the fee receipt from the student portal.",
     "keywords": "receipt fee portal", "category": cat2},
]

df = pd.DataFrame(fixed_entries + personal_entries)
print(df)

# Q2. scoring function - returns matching entries ranked by confidence
def score_query(query, df):
    query_words = query.lower().split()
    results = []
    for i, row in df.iterrows():
        text = (row["question"] + " " + row["keywords"]).lower()
        score = 0
        for w in query_words:
            if w in text:
                score += 1
        if score > 0:
            results.append((row["question"], row["answer"], score))
    results.sort(key=lambda x: x[2], reverse=True)
    return results

print("\nquery: fee")
for r in score_query("fee", df):
    print(r)

# Q3. same_category function
def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]

print("\nquestions in category:", cat1)
print(same_category(cat1, df))

# Q4. add a keyword to one entry and save to csv
new_keyword = input("\nenter a new keyword to add to first entry: ")
df.loc[0, "keywords"] = df.loc[0, "keywords"] + " " + new_keyword
df.to_csv(roll_number + "_faq_data.csv", index=False)
print("saved", roll_number + "_faq_data.csv")

# Q5. groupby category, count entries
print("\nentries per category:")
print(df.groupby("category").size())

# Q6. scoring function that prints all entries in case of a tie
def score_query_v2(query, df):
    query_words = query.lower().split()
    results = []
    for i, row in df.iterrows():
        text = (row["question"] + " " + row["keywords"]).lower()
        score = 0
        for w in query_words:
            if w in text:
                score += 1
        if score > 0:
            results.append((row["question"], row["answer"], score))

    if not results:
        print("no match found")
        return

    best = max(r[2] for r in results)
    top_matches = [r for r in results if r[2] == best]

    if len(top_matches) > 1:
        print("tie found, all top matches:")
        for m in top_matches:
            print(m)
    else:
        print(top_matches[0])

print("\nquery: fee (should tie)")
score_query_v2("fee", df)

print("\nquery: password (should not tie)")
score_query_v2("password", df)
