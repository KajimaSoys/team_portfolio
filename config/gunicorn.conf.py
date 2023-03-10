bind = "127.0.0.1:8001"
workers = 2
user = "kajimasoys"
timeout = 120

raw_env = [
    'TEAM_PORTFOLIO_DEBUG=$TEAM_PORTFOLIO_DEBUG',
    'TEAM_PORTFOLIO_ALLOWED_HOSTS=$TEAM_PORTFOLIO_ALLOWED_HOSTS',
    'TEAM_PORTFOLIO_SECRET_KEY=$TEAM_PORTFOLIO_SECRET_KEY',
    'TEAM_PORTFOLIO_POSTGRES_NAME=$TEAM_PORTFOLIO_POSTGRES_NAME',
    'TEAM_PORTFOLIO_POSTGRES_USER=$TEAM_PORTFOLIO_POSTGRES_USER',
    'TEAM_PORTFOLIO_POSTGRES_PASSWORD=$TEAM_PORTFOLIO_POSTGRES_PASSWORD',
    'TEAM_PORTFOLIO_POSTGRES_HOST=$TEAM_PORTFOLIO_POSTGRES_HOST',
    'TEAM_PORTFOLIO_POSTGRES_PORT=$TEAM_PORTFOLIO_POSTGRES_PORT',
    'TEAM_PORTFOLIO_CSRF_COOKIE_SECURE=$TEAM_PORTFOLIO_CSRF_COOKIE_SECURE',
    'TEAM_PORTFOLIO_SESSION_COOKIE_SECURE=$TEAM_PORTFOLIO_SESSION_COOKIE_SECURE'
]
