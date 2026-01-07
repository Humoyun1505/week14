tweets = [
    "I love coding! #Python #coding #Life",
    "Just learned #coding and lists in #PYTHON",
    "#life is good but #coding is better",
    "Ignore this #viral #FYP post"
]

banned = {"#viral", "#fyp"}
def analyze_trends(tweets, banned_tags):
    banned_tags = {tag.lower() for tag in banned_tags}
    counts = {}

    for tweet in tweets:
        for word in tweet.split():
            if word.startswith("#"):
                tag = word.lower()
                if tag not in banned_tags:
                    counts[tag] = counts.get(tag, 0) + 1

    sorted_tags = sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )

    return sorted_tags[:3]

print(analyze_trends(tweets, banned))


