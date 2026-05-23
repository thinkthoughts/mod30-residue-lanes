notebook00:
	jupyter nbconvert --execute --to notebook notebooks/00_foundations.ipynb

notebook01:
	jupyter nbconvert --execute --to notebook notebooks/01_lane_residue_01.ipynb

all:
	@echo "Run notebooks manually in Colab or locally."
