-- Indexes first letter of name and score in table names

CREATE INDEX idx_name_first_score ON names (name(1), score);
