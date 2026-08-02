import subprocess

def run_all():
    print("Running Master Aurora Build Engine...")
    subprocess.run(["python", "build_aurora_theme.py"], check=True)
    subprocess.run(["python", "build_next_level_assets.py"], check=True)
    subprocess.run(["python", "build_tier2_assets.py"], check=True)
    subprocess.run(["python", "build_tier3_assets.py"], check=True)
    subprocess.run(["python", "build_tier4_assets.py"], check=True)
    subprocess.run(["python", "build_tier5_assets.py"], check=True)
    print("MASTER AURORA BUILD COMPLETE & ALL SVGs VALIDATED!")

if __name__ == "__main__":
    run_all()
