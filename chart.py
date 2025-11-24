
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from pathlib import Path

def main():
    np.random.seed(42)

    channels = {
        "Email":     {"n": 700, "logmean": 2.6, "logsigma": 0.55},
        "Chat":      {"n": 800, "logmean": 1.7, "logsigma": 0.35},
        "Phone":     {"n": 650, "logmean": 2.1, "logsigma": 0.40},
        "Social":    {"n": 450, "logmean": 2.3, "logsigma": 0.50},
        "In‑App":    {"n": 500, "logmean": 1.9, "logsigma": 0.45},
    }

    records = []
    for ch, spec in channels.items():
        n = spec["n"]
        base = np.random.lognormal(mean=spec["logmean"], sigma=spec["logsigma"], size=n)
        base = np.clip(base, 0.5, 240)
        outlier_mask = np.random.rand(n) < 0.03
        base[outlier_mask] *= np.random.uniform(2, 4, size=outlier_mask.sum())
        base = np.clip(base, 0.5, 480)
        for v in base:
            records.append({"Channel": ch, "Response (minutes)": float(v)})

    df = pd.DataFrame.from_records(records)

    sns.set_style("whitegrid")
    sns.set_context("talk")

    plt.figure(figsize=(8, 8))
    ax = sns.violinplot(
        data=df,
        x="Channel",
        y="Response (minutes)",
        palette="Set2",
        inner="quartile",
        cut=0,
        scale="width"
    )

    ax.set_title("Customer Support Response Time Distribution by Channel", pad=14)
    ax.set_xlabel("Support Channel")
    ax.set_ylabel("Response Time (minutes)")

    ax.set_ylim(0, min(500, df["Response (minutes)"].max()*1.05))
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)

    plt.tight_layout()

    # First save with bbox_inches='tight' as required
    tmp_path = Path("chart_tmp.png")
    final_path = Path("chart.png")
    plt.savefig(tmp_path, dpi=64, bbox_inches="tight")
    plt.close()

    # Then pad or center-canvas to EXACTLY 512x512 while preserving tight layout
    im = Image.open(tmp_path).convert("RGBA")
    canvas = Image.new("RGBA", (512, 512), (255, 255, 255, 0))  # transparent background
    x = (512 - im.width) // 2
    y = (512 - im.height) // 2
    canvas.paste(im, (x, y), im)
    canvas = canvas.convert("RGB")
    canvas.save(final_path, format="PNG")

if __name__ == "__main__":
    main()
