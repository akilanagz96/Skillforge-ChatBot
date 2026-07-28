class QueryRouter:

    ROUTES = {
        "catalog": [
            "courses do you offer",
            "courses are available",
            "available courses",
            "what courses",
            "show me courses",
            "list courses",
            "which courses",
        ],

        "payment": [
            "payment",
            "pay",
            "fee",
            "fees",
            "emi",
            "installment",
            "installments",
            "monthly payment",
            "payment plan",
        ],

        "refund": [
            "refund",
            "cancel",
            "cancellation",
            "withdraw",
            "money back",
        ],

        "scholarship": [
            "scholarship",
            "discount",
            "financial aid",
        ],

        "admissions": [
            "admission",
            "admissions",
            "eligibility",
            "eligible",
            "apply",
            "application",
            "enroll",
            "enrollment",
            "requirements",
        ],

        "placement": [
            "placement",
            "placements",
            "job",
            "jobs",
            "career",
            "salary",
            "recruiter",
            "company hiring",
        ],

        "student": [
            "attendance",
            "absence",
            "leave",
            "live class",
            "live classes",
            "live session",
            "mentor",
            "assignment",
            "assignments",
            "holiday",
            "miss class",
        ],

        "contact": [
            "contact",
            "phone",
            "email",
            "office",
            "support",
            "address",
        ],

        "privacy": [
            "privacy",
            "personal data",
            "data protection",
        ],

        "terms": [
            "terms",
            "conditions",
            "agreement",
        ],

        "faq": [
            "faq",
            "frequently asked questions",
        ],
    }

    def is_catalog_query(self, question: str) -> bool:
        question = question.lower()

        return any(
            keyword in question
            for keyword in self.ROUTES["catalog"]
        )

    def route(self, question: str) -> str:

        question = question.lower()

        for route, keywords in self.ROUTES.items():

            if route == "catalog":
                continue

            if any(keyword in question for keyword in keywords):
                return route

        return "general"