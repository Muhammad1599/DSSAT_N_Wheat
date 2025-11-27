# Duernast DSSAT Wheat Analysis - Generalized Pipeline

A unified, production-ready pipeline for running DSSAT N-Wheat simulations, generating comprehensive visualizations, and performing statistical model evaluation for multiple Duernast experiments (2015, 2017, and future years).

## Overview

This repository contains a **generalized pipeline** that provides complete crop simulation analysis from model execution to statistical evaluation. The pipeline automatically handles:
- File naming differences between experiments
- Multi-year vs single-year simulations
- DAS normalization for winter wheat
- Dynamic visualization generation
- Comprehensive model evaluation for all 15 treatments

## Repository Structure

```
duernast 2015 DSSAT WWheat/
├── GENERALIZED_PIPELINE/          # Main pipeline
│   ├── config.py                  # Experiment configurations
│   ├── MASTER_WORKFLOW.py         # Unified workflow orchestrator
│   ├── create_duernast_visualizations.py  # 12-panel comprehensive visualization
│   ├── model_evaluation_analysis.py       # 8-panel model evaluation
│   └── requirements.txt           # Python dependencies
│
├── DUERNAST2015/                  # 2015 Experiment Data
│   ├── input/                     # Input files (WHX, WTH, WHA, WHT, SOL)
│   │   └── orignal data/          # Observed field data (.WHT)
│   ├── Genotype/                  # Cultivar parameters (CUL, ECO, SPE)
│   └── output/                    # Generated outputs
│       ├── *.OUT                  # DSSAT output files
│       ├── *_comprehensive_analysis.png/pdf  # 12-panel visualization
│       └── Model_analysis/       # Model evaluation outputs
│           ├── *_model_evaluation.png/pdf     # 8-panel evaluation
│           ├── *_comparison_all_treatments.csv # Detailed comparison
│           └── *_model_metrics_summary.csv    # Statistical metrics
│
├── DUERNAST2017/                  # 2017 Experiment Data
│   ├── input/                     # Input files (WHX, WTH, WHA, WHT, SOL)
│   │   └── orignal data/          # Observed field data (.WHT)
│   ├── Genotype/                  # Cultivar parameters (CUL, ECO, SPE)
│   └── output/                    # Generated outputs (same structure as 2015)
│
└── DSSAT48/                       # DSSAT v4.8 installation (required for simulation)
    ├── DSCSM048.EXE               # DSSAT executable
    └── [DSSAT files...]
```

## Quick Start

### 1. Install Dependencies

```bash
cd GENERALIZED_PIPELINE
pip install -r requirements.txt
```

### 2. Run Single Experiment

```bash
cd GENERALIZED_PIPELINE
python MASTER_WORKFLOW.py 2015    # Run 2015 experiment
python MASTER_WORKFLOW.py 2017    # Run 2017 experiment
```

### 3. Run All Experiments

```bash
cd GENERALIZED_PIPELINE
python MASTER_WORKFLOW.py --all
```

### 4. List Available Experiments

```bash
cd GENERALIZED_PIPELINE
python MASTER_WORKFLOW.py --list
```

## Workflow Overview

The pipeline executes a complete 4-step workflow automatically:

### Step 1: Prerequisites Check
- Validates required input files (WHX, WTH, WHA, WHT, SOL)
- Checks Python dependencies
- Verifies DSSAT executable availability
- Confirms output directory structure

### Step 2: DSSAT N-Wheat Simulation
- Copies input files to output directory
- Runs DSSAT model for all 15 nitrogen treatments
- Generates simulation output files (Summary.OUT, PlantGro.OUT, PlantN.OUT, etc.)

### Step 3: Comprehensive Visualization Generation
- Creates 12-panel scientific figure showing:
  - Weather data (temperature, precipitation, radiation)
  - Growth dynamics (biomass, LAI, plant height)
  - Nitrogen dynamics (plant N, grain N, N uptake)
  - Yield components (grain weight, harvest index)
- Displays 3 representative treatments (Control, Medium N, High N)
- Outputs: PNG and PDF formats

### Step 4: Model Evaluation and Statistical Analysis
- Extracts observed and simulated data for all 15 treatments
- Calculates statistical metrics (RMSE, MAE, R², Model Efficiency, Bias)
- Generates 8-panel evaluation visualization:
  - Yield, grain weight, and grain nitrogen scatter plots
  - Treatment-specific error analysis
  - Performance ranking and efficiency metrics
  - Summary statistics table
- Outputs: CSV files (comparison and metrics) + PNG and PDF visualizations

## Output Files

Each experiment generates outputs in its `output/` directory:

### Comprehensive Visualization (12 Panels)
- `duernast_2015_comprehensive_analysis.png` (or `duernast_2017_...`)
- `duernast_2015_comprehensive_analysis.pdf`
- Shows: Weather, biomass, LAI, plant height, nitrogen dynamics, grain weight, harvest index
- Displays: 3 representative treatments (Control, Medium N, High N)

### Model Evaluation (8 Panels)
- `Model_analysis/duernast_2015_model_evaluation.png`
- `Model_analysis/duernast_2015_model_evaluation.pdf`
- `Model_analysis/duernast_2015_comparison_all_treatments.csv` - Detailed data comparison
- `Model_analysis/duernast_2015_model_metrics_summary.csv` - Statistical metrics (R², RMSE, MAE, Model Efficiency, Bias)
- Shows: Scatter plots, error analysis, performance ranking, efficiency metrics for all 15 treatments

### DSSAT Outputs
- `Summary.OUT` - Main results
- `PlantGro.OUT` - Growth time series
- `PlantN.OUT` - Nitrogen dynamics
- `Weather.OUT` - Weather processing
- `SoilWat.OUT` - Water balance
- `SoilNi.OUT` - Soil nitrogen
- `OVERVIEW.OUT` - Treatment overview
- Additional DSSAT output files

## Configuration

Experiments are configured in `GENERALIZED_PIPELINE/config.py`. The configuration defines:

- Experiment year and name
- File prefixes (e.g., TUDU1501, TUDU1701)
- Output prefixes (e.g., duernast_2015, duernast_2017)
- Crop type (Spring Wheat, Winter Wheat)
- Multi-year simulation settings
- DAS normalization requirements
- Additional weather files (for multi-year simulations)

Example configuration:
```python
EXPERIMENTS = {
    2015: ExperimentConfig(
        year=2015,
        file_prefix="TUDU1501",
        output_prefix="duernast_2015",
        is_multi_year=False,
        normalize_das=False,
        crop_type="Spring Wheat",
        experiment_dir="DUERNAST2015",
        ...
    ),
    2017: ExperimentConfig(
        year=2017,
        file_prefix="TUDU1701",
        output_prefix="duernast_2017",
        is_multi_year=True,
        normalize_das=True,
        crop_type="Winter Wheat",
        experiment_dir="DUERNAST2017",
        additional_weather_file="TUDU1601.WTH",
        ...
    )
}
```

## Adding New Experiments

To add a new experiment year:

1. **Add configuration to `GENERALIZED_PIPELINE/config.py`**:
```python
EXPERIMENTS[2020] = ExperimentConfig(
    year=2020,
    experiment_name="DUERNAST2020",
    file_prefix="TUDU2001",
    output_prefix="duernast_2020",
    crop_type="Spring Wheat",
    is_multi_year=False,
    normalize_das=False,
    additional_weather_file=None,
    experiment_dir="DUERNAST2020"
)
```

2. **Ensure experiment directory structure matches**:
```
DUERNAST2020/
├── input/
│   ├── TUDU2001.WHX
│   ├── TUDU2001.WTH
│   ├── TUDU2001.WHA
│   ├── TUDU2001.WHT (in input/orignal data/)
│   └── DE.SOL
├── Genotype/
│   ├── WHAPS048.CUL
│   ├── WHAPS048.ECO
│   └── WHAPS048.SPE
└── output/  (created automatically)
```

3. **Run the experiment**:
```bash
cd GENERALIZED_PIPELINE
python MASTER_WORKFLOW.py 2020
```

## Requirements

- Python 3.7+
- pandas >= 1.3.0
- numpy >= 1.21.0
- matplotlib >= 3.4.0
- seaborn >= 0.11.0
- DSSAT v4.8 (DSCSM048.EXE)

Install dependencies:
```bash
cd GENERALIZED_PIPELINE
pip install -r requirements.txt
```

## Experiment Details

### 2015 Experiment
- **Crop**: Spring Wheat
- **Sowing**: Day 70 (March 11, 2015)
- **Treatments**: 15 nitrogen treatments
- **File Prefix**: TUDU1501
- **Model**: N-Wheat (WHAPS048)

### 2017 Experiment
- **Crop**: Winter Wheat
- **Sowing**: Day 298 (October 25, 2016)
- **Treatments**: 15 nitrogen treatments
- **File Prefix**: TUDU1701
- **Multi-year**: Requires weather data for 2016-2017
- **Model**: N-Wheat (WHAPS048)

## Model Evaluation Metrics

The model evaluation component provides comprehensive statistical analysis for all 15 treatments:

- **R² (Coefficient of Determination)**: Proportion of variance explained (0-1, higher is better, 1 = perfect)
- **RMSE (Root Mean Squared Error)**: Average magnitude of prediction errors (lower is better, 0 = perfect)
- **MAE (Mean Absolute Error)**: Average absolute difference between simulated and observed (lower is better, 0 = perfect)
- **Model Efficiency (Nash-Sutcliffe)**: Normalized performance metric (>0.5 = good, 1 = perfect, <0 = model worse than using mean)
- **Bias**: Systematic over/underestimation tendency (positive = overestimation, negative = underestimation)

Metrics are calculated for:
- **Yield** (kg/ha)
- **Grain Weight** (mg/grain)
- **Grain Nitrogen** (kg N/ha)

All 15 treatments are included in the statistical analysis, with visualizations showing treatment-specific performance and a top legend mapping treatment numbers to nitrogen amounts.

## Troubleshooting

### "Experiment directory not found"
- Ensure you're running from project root or GENERALIZED_PIPELINE directory
- Check that experiment directory (e.g., DUERNAST2015) exists

### "Missing input files"
- Verify input files exist in `{experiment_dir}/input/`
- Check file naming matches `file_prefix` in config
- Ensure observed data file (.WHT) is in `input/orignal data/`

### "Visualization script not found"
- The workflow uses scripts from `GENERALIZED_PIPELINE/`
- Ensure `create_duernast_visualizations.py` and `model_evaluation_analysis.py` exist

### "DSSAT simulation failed"
- Verify DSSAT executable (DSCSM048.EXE) is accessible
- Check input file formats are correct
- Review DSSAT output files for error messages

## Documentation

Additional documentation files in the repository:

- `MODEL_EVALUATION_VISUALIZATION_DOCUMENTATION.txt` - Detailed explanation of model evaluation plots, metrics, and interpretation
- `VISUALIZATION_TECHNICAL_DOCUMENTATION.txt` - Technical details of comprehensive 12-panel visualization
- `SRGF_OPTIMIZATION_DOCUMENTATION.txt` - Soil root growth factor optimization methodology
- `INITIAL_CONDITIONS_CSM_PIPELINE_METHODOLOGY.txt` - Initial soil conditions calculation approach
- `CSMTOOLS_DATA_CONVERSION_PIPELINE.txt` - Data conversion pipeline documentation
- `DATA_COMPARISON_ANALYSIS.txt` - Comparison between original and current input data files
- `THESIS_STRUCTURE_AND_STORYLINE.txt` - Thesis structure and research storyline

## Key Features

- **Complete Workflow**: Prerequisites check → Simulation → Visualization → Model Evaluation
- **Automatic Configuration**: Experiment parameters defined in `config.py`
- **Conditional Logic**: Handles differences (multi-year, DAS normalization) automatically
- **Comprehensive Outputs**: 12-panel visualization + 8-panel model evaluation
- **Statistical Analysis**: Complete metrics for all 15 treatments
- **Easy Extension**: Add new experiments by adding to `config.py`
- **Production Ready**: Tested and validated with multiple experiments

## Status

**Production Ready**: The generalized pipeline has been tested and validated with both 2015 and 2017 experiments. All workflows complete successfully with 100% success rate.

---

**Last Updated**: 2025-11-27  
**Version**: 2.0 (Generalized Pipeline with Model Evaluation)
