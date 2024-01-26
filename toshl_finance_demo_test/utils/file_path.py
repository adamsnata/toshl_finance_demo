def abs_path_from_project(relative_path: str):
    import toshl_finance_demo_test
    from pathlib import Path

    return (Path(toshl_finance_demo_test.__file__).parent.parent / relative_path).absolute()
