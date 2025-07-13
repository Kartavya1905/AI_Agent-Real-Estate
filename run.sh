bash
# Exit immediately if a command fails
set -e

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📥 Installing packages..."
pip install -r requirements.txt

# Load .env if available
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
  echo "🔐 Loaded environment variables from .env"
fi

# Start FastAPI app
echo "🚀 Launching FastAPI on http://localhost:8000 ..."
uvicorn main:app --reload --host 0.0.0.0 --port 8000
