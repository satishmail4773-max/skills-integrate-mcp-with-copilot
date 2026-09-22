import app


def test_github_skills_activity_is_available():
    activities = app.activities

    assert "GitHub Skills" in activities
    assert activities["GitHub Skills"]["description"] == (
        "Learn practical coding and collaboration skills with GitHub"
    )
