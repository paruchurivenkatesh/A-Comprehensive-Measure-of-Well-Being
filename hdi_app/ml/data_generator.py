import pandas as pd
import numpy as np
import os

def generate_synthetic_dataset(filepath):
    """
    Generates a synthetic HDI dataset mimicking the Kaggle dataset structure.
    Useful for development when the real dataset is not immediately available.
    """
    print("Generating synthetic HDI dataset...")
    
    np.random.seed(42)
    n_samples = 200
    
    # Generate random country names
    countries = [f"Country_{i}" for i in range(1, n_samples + 1)]
    regions = np.random.choice(['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania'], n_samples)
    
    # Generate features with realistic correlations
    # Very High HDI characteristics: high LE, high Schooling, high GNI
    # Low HDI characteristics: low LE, low Schooling, low GNI
    
    base_factor = np.random.rand(n_samples) # 0 to 1, representing underlying development factor
    
    life_expectancy = 50 + (base_factor * 35) + np.random.normal(0, 3, n_samples)
    life_expectancy = np.clip(life_expectancy, 45, 85)
    
    expected_years_schooling = 8 + (base_factor * 12) + np.random.normal(0, 1.5, n_samples)
    expected_years_schooling = np.clip(expected_years_schooling, 5, 22)
    
    mean_years_schooling = 3 + (base_factor * 10) + np.random.normal(0, 1.5, n_samples)
    mean_years_schooling = np.clip(mean_years_schooling, 1.5, 14.5)
    
    # GNI per capita grows exponentially with the development factor
    gni_per_capita = 1000 + (np.exp(base_factor * 4) * 1000) + np.random.normal(0, 2000, n_samples)
    gni_per_capita = np.clip(gni_per_capita, 800, 120000)
    
    # Calculate a proxy HDI score based on the indicators (simplified UNDP formula)
    # LE index: (LE - 20) / (85 - 20)
    # Edu index: (MYS/15 + EYS/18) / 2
    # GNI index: (ln(GNI) - ln(100)) / (ln(75000) - ln(100))
    # HDI = geometric mean of the three indices
    
    le_index = (life_expectancy - 20) / 65
    le_index = np.clip(le_index, 0, 1)
    
    edu_index = ((mean_years_schooling / 15) + (expected_years_schooling / 18)) / 2
    edu_index = np.clip(edu_index, 0, 1)
    
    gni_index = (np.log(gni_per_capita) - np.log(100)) / (np.log(75000) - np.log(100))
    gni_index = np.clip(gni_index, 0, 1)
    
    hdi_score = np.cbrt(le_index * edu_index * gni_index)
    
    # Add some noise to the HDI score
    hdi_score = hdi_score + np.random.normal(0, 0.02, n_samples)
    hdi_score = np.clip(hdi_score, 0.350, 0.990)
    
    # Categorize
    hdi_category = []
    for score in hdi_score:
        if score >= 0.800:
            hdi_category.append('Very High')
        elif score >= 0.700:
            hdi_category.append('High')
        elif score >= 0.550:
            hdi_category.append('Medium')
        else:
            hdi_category.append('Low')
            
    # Rank
    hdi_rank = np.argsort(hdi_score)[::-1].argsort() + 1
    
    # Create DataFrame
    df = pd.DataFrame({
        'Country': countries,
        'Region': regions,
        'Life Expectancy': life_expectancy,
        'Expected Years of Schooling': expected_years_schooling,
        'Mean Years of Schooling': mean_years_schooling,
        'Gross National Income Per Capita': gni_per_capita,
        'HDI Score': hdi_score,
        'HDI Rank': hdi_rank,
        'HDI Category': hdi_category
    })
    
    # Introduce some missing values to test preprocessing
    df.loc[np.random.choice(df.index, 5), 'Life Expectancy'] = np.nan
    df.loc[np.random.choice(df.index, 3), 'Gross National Income Per Capita'] = np.nan
    
    # Save to CSV
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Synthetic dataset saved to {filepath}")
    return filepath

if __name__ == "__main__":
    # Execute if run standalone
    target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'dataset', 'raw', 'hdi_data.csv'))
    generate_synthetic_dataset(target_path)
