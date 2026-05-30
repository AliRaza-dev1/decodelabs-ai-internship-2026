from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


JOB_ROLES = [
    {
        "title": "AI / ML Engineer",
        "skills": "python machine learning deep learning tensorflow pytorch numpy pandas scikit-learn data neural networks algorithms"
    },
    {
        "title": "Data Scientist",
        "skills": "python statistics data analysis numpy pandas matplotlib sql machine learning visualization regression classification"
    },
    {
        "title": "Data Analyst",
        "skills": "sql excel data analysis tableau power bi statistics reporting visualization business intelligence python"
    },
    {
        "title": "Backend Developer",
        "skills": "python java nodejs apis rest sql databases django flask postgresql mongodb server authentication"
    },
    {
        "title": "Frontend Developer",
        "skills": "javascript html css react vuejs typescript responsive design ui ux web components dom bootstrap"
    },
    {
        "title": "Full Stack Developer",
        "skills": "javascript python html css react nodejs sql rest apis mongodb postgresql git databases"
    },
    {
        "title": "DevOps Engineer",
        "skills": "aws docker kubernetes linux ci cd git jenkins cloud infrastructure automation terraform bash scripting"
    },
    {
        "title": "Cloud Architect",
        "skills": "aws azure google cloud infrastructure networking security terraform kubernetes docker scalability microservices"
    },
    {
        "title": "Cybersecurity Analyst",
        "skills": "networking security linux python penetration testing firewalls encryption protocols threat analysis ethical hacking"
    },
    {
        "title": "Mobile Developer",
        "skills": "flutter dart swift kotlin android ios react native mobile ui apis firebase java"
    },
    {
        "title": "Database Administrator",
        "skills": "sql mysql postgresql oracle mongodb database design optimization queries indexing backup recovery performance"
    },
    {
        "title": "NLP Engineer",
        "skills": "python nlp text processing transformers bert gpt huggingface tokenization sentiment analysis named entity recognition"
    },
]


def get_user_skills():
    print("=" * 60)
    print("  TECH STACK RECOMMENDER  |  DecodeLabs 2026")
    print("  Content-Based Filtering  |  TF-IDF + Cosine Similarity")
    print("=" * 60)
    print()
    print("  Enter your skills one by one.")
    print("  Minimum 3 skills required for accurate matching.")
    print("  Press Enter with no input when done.")
    print()

    skills = []
    count = 1

    while True:
        skill = input("  Skill " + str(count) + " : ").strip().lower()

        if skill == "":
            if len(skills) < 3:
                print("  Please enter at least " + str(3 - len(skills)) + " more skill(s).")
                continue
            else:
                break

        if skill in skills:
            print("  Skill already added. Try a different one.")
            continue

        skills.append(skill)
        count += 1

    return skills


def build_corpus(user_skills):
    user_profile = " ".join(user_skills)
    corpus = [user_profile]
    for role in JOB_ROLES:
        corpus.append(role["skills"])
    return corpus


def compute_similarity(corpus):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    user_vector = tfidf_matrix[0]
    role_vectors = tfidf_matrix[1:]
    scores = cosine_similarity(user_vector, role_vectors)[0]
    return scores


def rank_and_filter(scores, top_n=3):
    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked[:top_n]


def display_results(user_skills, top_matches):
    print()
    print("=" * 60)
    print("  YOUR PROFILE")
    print("=" * 60)
    print("  Skills : " + ", ".join(user_skills))
    print()
    print("=" * 60)
    print("  TOP " + str(len(top_matches)) + " RECOMMENDED JOB ROLES")
    print("=" * 60)
    print()

    for rank, (index, score) in enumerate(top_matches, start=1):
        title = JOB_ROLES[index]["title"]
        match_percent = round(score * 100, 2)

        bar_filled = int(score * 20)
        bar = "[" + "#" * bar_filled + "-" * (20 - bar_filled) + "]"

        print("  Rank " + str(rank) + " : " + title)
        print("  Score  : " + bar + " " + str(match_percent) + "%")
        print("  Skills : " + JOB_ROLES[index]["skills"])
        print()

    if top_matches[0][1] == 0:
        print("  No strong matches found.")
        print("  Try adding more specific technical skills.")
        print()


def main():
    print()

    user_skills = get_user_skills()

    print()
    print("  Processing your profile...")
    print()

    corpus  = build_corpus(user_skills)
    scores  = compute_similarity(corpus)
    top_matches = rank_and_filter(scores, top_n=3)

    display_results(user_skills, top_matches)

    print("=" * 60)
    print("  Pipeline Complete.")
    print("  Steps: Ingestion -> Scoring -> Sorting -> Filtering")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
