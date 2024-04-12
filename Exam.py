# Importing libraries
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Generate synthetic dataset
np.random.seed(42)
num_students = 1000
num_questions = 20
num_subjects = 5
subjects = ['Language', 'Physics', 'Chemistry', 'Mathematics']
language_preferences = ['English', 'Hindi', 'Marathi', 'Tamil']

data = {
    'Student_ID': np.arange(1, num_students + 1),
    'Language': np.random.choice(language_preferences, size=num_students),
}
