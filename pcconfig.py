import pynecone as pc

class LoginreflexConfig(pc.Config):
    pass

config = LoginreflexConfig(
    app_name="login_reflex",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)