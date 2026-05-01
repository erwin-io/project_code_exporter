import os
import argparse
from datetime import datetime
from pathlib import Path


PRESETS = {
    "ionic": {
        "include_ext": {
            ".ts", ".html", ".scss", ".css", ".json", ".js", ".mjs",
            ".xml", ".yml", ".yaml", ".md"
        },
        "include_files": {
            "package.json",
            "angular.json",
            "ionic.config.json",
            "capacitor.config.ts",
            "capacitor.config.json",
            "tsconfig.json",
            "tsconfig.app.json",
            "tsconfig.spec.json",
            "proxy.conf.json",
            ".env",
            ".env.local",
            ".env.production",
            ".env.development",
            "README.md",
        },
        "include_dirs": {
            "src",
        },
    },

    "angular": {
        "include_ext": {
            ".ts", ".html", ".scss", ".css", ".json", ".js", ".mjs",
            ".yml", ".yaml", ".md"
        },
        "include_files": {
            "package.json",
            "angular.json",
            "tsconfig.json",
            "tsconfig.app.json",
            "tsconfig.spec.json",
            "proxy.conf.json",
            ".env",
            ".env.local",
            ".env.production",
            ".env.development",
            "README.md",
        },
        "include_dirs": {
            "src",
        },
    },

    "node": {
        "include_ext": {
            ".js", ".ts", ".json", ".mjs", ".cjs",
            ".env", ".md", ".yml", ".yaml"
        },
        "include_files": {
            "package.json",
            "package-lock.json",
            "pnpm-lock.yaml",
            "yarn.lock",
            "tsconfig.json",
            ".env",
            ".env.local",
            ".env.production",
            ".env.development",
            "nodemon.json",
            "README.md",
        },
        "include_dirs": {
            "src",
            "routes",
            "controllers",
            "services",
            "models",
            "config",
            "middleware",
            "middlewares",
            "utils",
            "database",
            "db",
            "public",
            "views",
        },
    },

    "python": {
        "include_ext": {
            ".py", ".json", ".txt", ".md", ".toml", ".ini",
            ".yml", ".yaml", ".env"
        },
        "include_files": {
            "requirements.txt",
            "pyproject.toml",
            "Pipfile",
            "Pipfile.lock",
            ".env",
            ".env.local",
            ".env.production",
            ".env.development",
            "README.md",
        },
        "include_dirs": {
            "app",
            "src",
            "api",
            "services",
            "models",
            "routes",
            "routers",
            "config",
            "utils",
            "templates",
        },
    },

    "all": {
        "include_ext": {
            ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
            ".html", ".css", ".scss", ".sass",
            ".json", ".xml", ".md",
            ".py", ".java", ".cs", ".cpp", ".c", ".h",
            ".yml", ".yaml", ".toml", ".ini",
            ".env"
        },
        "include_files": set(),
        "include_dirs": set(),
    },
}


DEFAULT_EXCLUDE_DIRS = {
    "node_modules",
    ".git",
    ".vscode",
    ".idea",
    "dist",
    "build",
    "www",
    "android",
    "ios",
    "coverage",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
    "env",
    ".next",
    ".nuxt",
    ".angular",
    ".turbo",
    ".cache",
    "logs",
    "tmp",
    "temp",
}

DEFAULT_EXCLUDE_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".svg",
    ".mp4", ".mp3", ".wav", ".avi",
    ".zip", ".rar", ".7z", ".tar", ".gz",
    ".exe", ".dll", ".so",
    ".pdf", ".docx", ".xlsx",
    ".map",
}


def file_exists(root: Path, filename: str) -> bool:
    return (root / filename).exists()


def dir_exists(root: Path, dirname: str) -> bool:
    return (root / dirname).exists() and (root / dirname).is_dir()


def read_package_json_text(root: Path) -> str:
    package_path = root / "package.json"

    if not package_path.exists():
        return ""

    try:
        return package_path.read_text(encoding="utf-8", errors="ignore").lower()
    except Exception:
        return ""


def detect_project_type(root: Path) -> str | None:
    """
    Auto-detect project type from common project-level files.

    Priority:
    1. Ionic
    2. Angular
    3. Node.js
    4. Python
    """

    package_text = read_package_json_text(root)

    # Ionic / Capacitor Angular project
    if (
        file_exists(root, "ionic.config.json")
        or file_exists(root, "capacitor.config.ts")
        or file_exists(root, "capacitor.config.json")
        or "@ionic/angular" in package_text
        or "ionic" in package_text
    ):
        return "ionic"

    # Angular project
    if (
        file_exists(root, "angular.json")
        or "@angular/core" in package_text
        or "@angular/cli" in package_text
    ):
        return "angular"

    # Node.js / Express / NestJS project
    if file_exists(root, "package.json"):
        return "node"

    # Python project
    if (
        file_exists(root, "requirements.txt")
        or file_exists(root, "pyproject.toml")
        or file_exists(root, "Pipfile")
        or file_exists(root, "main.py")
        or dir_exists(root, "venv")
        or dir_exists(root, ".venv")
    ):
        return "python"

    # Check if folder contains many .py files
    py_count = 0
    for current_root, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDE_DIRS]

        for file in files:
            if file.endswith(".py"):
                py_count += 1

            if py_count >= 3:
                return "python"

    return None


def ask_user_for_preset() -> str:
    print()
    print("Could not auto-detect project type.")
    print()
    print("Choose project preset:")
    print("[1] Ionic / Angular")
    print("[2] Angular")
    print("[3] Node.js / Express / NestJS")
    print("[4] Python / FastAPI")
    print("[5] All common code files")
    print()

    choice = input("Enter choice: ").strip()

    if choice == "1":
        return "ionic"
    if choice == "2":
        return "angular"
    if choice == "3":
        return "node"
    if choice == "4":
        return "python"
    if choice == "5":
        return "all"

    print("Invalid choice. Using all.")
    return "all"


def is_probably_text_file(path: Path) -> bool:
    try:
        with open(path, "rb") as f:
            chunk = f.read(2048)

        if b"\0" in chunk:
            return False

        return True
    except Exception:
        return False


def should_include_file(path: Path, root: Path, preset: dict) -> bool:
    rel = path.relative_to(root)
    parts = set(rel.parts)

    if any(part in DEFAULT_EXCLUDE_DIRS for part in parts):
        return False

    if path.suffix.lower() in DEFAULT_EXCLUDE_EXT:
        return False

    filename = path.name
    ext = path.suffix.lower()

    include_ext = preset["include_ext"]
    include_files = preset["include_files"]
    include_dirs = preset["include_dirs"]

    if ext in include_ext or filename in include_files:
        if include_dirs:
            top_dir = rel.parts[0] if rel.parts else ""

            if top_dir in include_dirs or len(rel.parts) == 1:
                return True

            return False

        return True

    return False


def read_file_safely(path: Path) -> str:
    encodings = ["utf-8", "utf-8-sig", "cp1252", "latin-1"]

    for enc in encodings:
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
        except Exception as e:
            return f"[ERROR READING FILE: {e}]"

    return "[ERROR READING FILE: unsupported encoding]"


def collect_files(root: Path, preset_name: str):
    preset = PRESETS[preset_name]
    files = []

    for current_root, dirs, filenames in os.walk(root):
        dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDE_DIRS]

        for filename in filenames:
            path = Path(current_root) / filename

            if not path.is_file():
                continue

            if should_include_file(path, root, preset) and is_probably_text_file(path):
                files.append(path)

    return sorted(files, key=lambda p: str(p.relative_to(root)).lower())


def build_export_text(root: Path, files: list[Path], preset_name: str) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    lines.append("=" * 90)
    lines.append("PROJECT CODE EXPORT")
    lines.append("=" * 90)
    lines.append(f"Source Folder : {root}")
    lines.append(f"Preset        : {preset_name}")
    lines.append(f"Exported At   : {now}")
    lines.append(f"Total Files   : {len(files)}")
    lines.append("=" * 90)
    lines.append("")

    lines.append("FILE LIST")
    lines.append("-" * 90)

    for file in files:
        lines.append(str(file.relative_to(root)).replace("\\", "/"))

    lines.append("")
    lines.append("=" * 90)
    lines.append("FILE CONTENTS")
    lines.append("=" * 90)

    for file in files:
        rel = str(file.relative_to(root)).replace("\\", "/")
        content = read_file_safely(file)

        lines.append("")
        lines.append("=" * 90)
        lines.append(f"FILE: {rel}")
        lines.append("=" * 90)
        lines.append(content)
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Export selected project source files into one TXT file."
    )

    parser.add_argument(
        "project_dir",
        help="Project directory to export"
    )

    parser.add_argument(
        "--preset",
        choices=PRESETS.keys(),
        default=None,
        help="Optional project type preset: ionic, angular, node, python, all"
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Optional output TXT file path."
    )

    args = parser.parse_args()

    root = Path(args.project_dir).resolve()

    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Invalid project directory: {root}")

    if args.preset:
        preset_name = args.preset
        print(f"Using manual preset: {preset_name}")
    else:
        detected = detect_project_type(root)

        if detected:
            preset_name = detected
            print(f"Auto-detected project type: {preset_name}")
        else:
            preset_name = ask_user_for_preset()

    files = collect_files(root, preset_name)

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        safe_name = root.name.replace(" ", "_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = root / f"{safe_name}_export_{preset_name}_{timestamp}.txt"

    print(f"Exporting from: {root}")
    print(f"Preset: {preset_name}")
    print(f"Files found: {len(files)}")
    print(f"Output: {output_path}")

    text = build_export_text(root, files, preset_name)
    output_path.write_text(text, encoding="utf-8")

    print()
    print("Done.")


if __name__ == "__main__":
    main()