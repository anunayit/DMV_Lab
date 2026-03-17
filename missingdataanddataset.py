import pandas as pd
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
FILE_NAME = 'social_media_data.csv'

def run_data_analysis():
    # 1. LOAD DATA
    try:
        # skiprows=1 skips that empty first row seen in your image
        df = pd.read_csv(FILE_NAME, skiprows=1)
        
        # Clean up column names (removes hidden spaces and makes them lowercase for easier matching)
        df.columns = df.columns.str.strip().str.lower()
        
        print(f"Successfully loaded. Columns identified: {df.columns.tolist()}")
    except FileNotFoundError:
        print(f"Error: '{FILE_NAME}' not found in this folder.")
        return

    # 2. HANDLE MISSING DATA
    # We target 'likes' and 'comments' columns based on your sheet
    for col in ['likes', 'comments']:
        if col in df.columns:
            if df[col].isnull().any():
                print(f"\n[!] Missing data found in column: {col}")
                for index in df[df[col].isnull()].index:
                    # Identify the row by Platform or Post ID for the user
                    platform = df.at[index, 'platform']
                    post_id = df.at[index, 'post_id']
                    
                    user_val = input(f"   -> Enter {col} for {platform} (ID: {post_id}): ")
                    df.at[index, col] = float(user_val)
        else:
            print(f"Warning: Column '{col}' not found. Check your CSV headers.")

    # 3. DATA AGGREGATION
    # Group by platform to make the charts readable
    grouped = df.groupby('platform')['likes'].sum().reset_index()

    # 4. GENERATE VISUALIZATIONS
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('Social Media Data Analysis', fontsize=16)

    # Pie Chart
    axes[0].pie(grouped['likes'], labels=grouped['platform'], autopct='%1.1f%%', startangle=140)
    axes[0].set_title('Likes Distribution (%)')

    # Bar Chart
    axes[1].bar(grouped['platform'], grouped['likes'], color='skyblue')
    axes[1].set_title('Total Likes per Platform')
    axes[1].tick_params(axis='x', rotation=45)

    # Stair Chart
    # We use edges for the stair plot
    axes[2].stairs(grouped['likes'], fill=True, color='orange')
    axes[2].set_title('Platform Performance (Stair)')
    # Adding labels to the stair chart
    axes[2].set_xticks(range(len(grouped['platform'])))
    axes[2].set_xticklabels(grouped['platform'], rotation=45)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_data_analysis()
