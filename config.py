"""Read KEY=value setting from a .env file."""
def load_env(path=".env"):
	settings = ()
	with open(path) as handle:
		for line in handle:
			line = line.strip()
			if not line or line.startswith("#"):
				continue
			Key, _, value = line.partition("=")
			settings [key.strip()] = value.strip()
	return settings
