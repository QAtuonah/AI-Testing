# Input Data Quality

## Test Scenarios

1. Check for empty or null review fields.
2. Validate encoding of non-ASCII characters (e.g., emojis, accents).
3. Identify duplicate entries.
4. Detect outliers (e.g., all caps, spammy content).

## Expected Behavior
- Model should ignore invalid input or raise clear errors.
- All reviews should be processed as UTF-8.
