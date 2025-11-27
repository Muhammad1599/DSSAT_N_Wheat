#!/usr/bin/env python3
"""
Configuration module for generalized Duernast pipeline

Defines experiment configurations for different years and datasets.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class ExperimentConfig:
    """Configuration for a Duernast experiment"""
    
    # Experiment identification
    year: int
    experiment_name: str  # e.g., "DUERNAST2015" or "DUERNAST2017"
    
    # File naming
    file_prefix: str  # e.g., "TUDU1501" or "TUDU1701"
    output_prefix: str  # e.g., "duernast_2015" or "duernast_2017"
    
    # Experiment characteristics
    crop_type: str  # "Spring Wheat" or "Winter Wheat"
    is_multi_year: bool  # True for winter wheat (2017), False for spring wheat (2015)
    normalize_das: bool  # True if DAS should be normalized in visualization
    
    # Directory paths (relative to project root)
    experiment_dir: str  # e.g., "DUERNAST2015" or "DUERNAST2017"
    
    # Optional: additional weather file for multi-year simulations
    additional_weather_file: Optional[str] = None  # e.g., "TUDU1601.WTH" for 2017
    
    def __post_init__(self):
        """Validate configuration"""
        if self.is_multi_year and not self.additional_weather_file:
            raise ValueError(f"Multi-year experiment {self.year} requires additional_weather_file")
        if not self.is_multi_year and self.additional_weather_file:
            raise ValueError(f"Single-year experiment {self.year} should not have additional_weather_file")


# Predefined experiment configurations
EXPERIMENTS = {
    2015: ExperimentConfig(
        year=2015,
        experiment_name="DUERNAST2015",
        file_prefix="TUDU1501",
        output_prefix="duernast_2015",
        crop_type="Spring Wheat",
        is_multi_year=False,
        normalize_das=False,
        additional_weather_file=None,
        experiment_dir="DUERNAST2015"
    ),
    2017: ExperimentConfig(
        year=2017,
        experiment_name="DUERNAST2017",
        file_prefix="TUDU1701",
        output_prefix="duernast_2017",
        crop_type="Winter Wheat",
        is_multi_year=True,
        normalize_das=True,
        additional_weather_file="TUDU1601.WTH",
        experiment_dir="DUERNAST2017"
    )
}


def get_config(year: int) -> ExperimentConfig:
    """Get configuration for a specific year"""
    if year not in EXPERIMENTS:
        raise ValueError(f"No configuration found for year {year}. Available: {list(EXPERIMENTS.keys())}")
    return EXPERIMENTS[year]


def list_available_experiments():
    """List all available experiment configurations"""
    return list(EXPERIMENTS.keys())

