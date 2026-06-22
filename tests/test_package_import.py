from pathlib import Path

import oxide_screening
from oxide_screening.utils.config import load_yaml_config
from oxide_screening.utils.paths import ROOT_DIR


def test_package_imports() -> None:
    assert oxide_screening.__version__ == "0.1.0"


def test_project_root_exists() -> None:
    assert ROOT_DIR.exists()
    assert (ROOT_DIR / "pyproject.toml").exists()


def test_data_config_loads() -> None:
    config_path = ROOT_DIR / "configs" / "data.yaml"
    config = load_yaml_config(config_path)

    assert "materials_project" in config
    assert "query" in config
    assert "outputs" in config
    assert config["materials_project"]["api_key_env_var"] == "MP_API_KEY"


def test_descriptor_config_loads() -> None:
    config_path = ROOT_DIR / "configs" / "descriptors.yaml"
    config = load_yaml_config(config_path)

    assert "oxidation_states" in config
    assert "descriptor_filters" in config
    assert "molecular_oxyanion_b_elements" in config

    oxyanion_elements = config["molecular_oxyanion_b_elements"]
    assert "N" in oxyanion_elements
    assert "C" in oxyanion_elements
    assert "P" in oxyanion_elements