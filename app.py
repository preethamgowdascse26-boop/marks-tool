"""Marks Tool - print a short report for a list of marks."""
from config import load_env
from stats import average, highest
MARKS = [72, 65, 88, 91, 54]
def main():
	settings = load_env()
	print(settings["APP_NAME"])
	print("Count :", len(MARKS))
	print("Average:", average(MARKS))
	print("Highest:", highest(MARKS))
if __name__ == "__main__":
	main()
