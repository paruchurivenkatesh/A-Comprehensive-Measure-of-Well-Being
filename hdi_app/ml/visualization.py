import matplotlib
matplotlib.use('Agg') # Use non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

def generate_eda_plots(df, output_dir):
    """Generate and save EDA plots."""
    os.makedirs(output_dir, exist_ok=True)
    
    numerical_cols = ['Life Expectancy', 'Expected Years of Schooling', 'Mean Years of Schooling', 'Gross National Income Per Capita', 'HDI Score']
    
    # 1. Correlation Heatmap
    plt.figure(figsize=(10, 8))
    corr = df[numerical_cols].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap of HDI Indicators')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correlation_heatmap.png'))
    plt.close()
    
    # 2. Distribution Plot - HDI Score
    plt.figure(figsize=(10, 6))
    sns.histplot(df['HDI Score'], kde=True, bins=30, color='skyblue')
    plt.title('Distribution of HDI Scores')
    plt.xlabel('HDI Score')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'hdi_distribution.png'))
    plt.close()
    
    # 3. Scatter Plot - GNI vs HDI
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Gross National Income Per Capita', y='HDI Score', hue='HDI Category', data=df, palette='viridis')
    plt.xscale('log') # Log scale for GNI is usually better
    plt.title('GNI per Capita vs HDI Score')
    plt.xlabel('GNI per Capita (Log Scale)')
    plt.ylabel('HDI Score')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'gni_vs_hdi.png'))
    plt.close()

    # 4. Box Plot - HDI by Region (if Region exists)
    if 'Region' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='Region', y='HDI Score', data=df, palette='Set2')
        plt.title('HDI Score Distribution by Region')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'hdi_by_region.png'))
        plt.close()
        
    print(f"EDA plots saved to {output_dir}")
