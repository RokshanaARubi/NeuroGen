from dash import html, dcc

def create_assessment_layout():
    return html.Div([
        html.H1("Comprehensive Neurological Assessment", style={'textAlign': 'center', 'marginBottom': '30px'}),
        
        html.Div([
            # Cognitive Assessment Section
            html.Div([
                html.H2("Cognitive Screening", style={'color': '#6a46f0', 'marginBottom': '20px'}),
                html.P("This assessment helps screen for cognitive changes. Answer each question honestly.", 
                      style={'color': '#666', 'marginBottom': '30px'}),
                
                # MMSE-like Questions
                html.Div([
                    # Question 1: Orientation
                    html.Div([
                        html.H4("1. Orientation to Time", style={'marginBottom': '10px'}),
                        html.P("What is the current year, season, month, date, and day of the week?", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q1-orientation',
                            options=[
                                {'label': 'All 5 correct (5 points)', 'value': 5},
                                {'label': '4 correct (4 points)', 'value': 4},
                                {'label': '3 correct (3 points)', 'value': 3},
                                {'label': '2 correct (2 points)', 'value': 2},
                                {'label': '1 correct (1 point)', 'value': 1},
                                {'label': 'None correct (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 2: Registration
                    html.Div([
                        html.H4("2. Immediate Memory", style={'marginBottom': '10px'}),
                        html.P("Repeat these three words: 'apple', 'table', 'penny'", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q2-registration',
                            options=[
                                {'label': 'All 3 words repeated correctly (3 points)', 'value': 3},
                                {'label': '2 words correct (2 points)', 'value': 2},
                                {'label': '1 word correct (1 point)', 'value': 1},
                                {'label': 'None correct (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 3: Attention and Calculation
                    html.Div([
                        html.H4("3. Attention and Calculation", style={'marginBottom': '10px'}),
                        html.P("Starting from 100, subtract 7, then keep subtracting 7 from each new number.", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q3-calculation',
                            options=[
                                {'label': 'All 5 subtractions correct (5 points)', 'value': 5},
                                {'label': '3-4 correct (3 points)', 'value': 3},
                                {'label': '1-2 correct (1 point)', 'value': 1},
                                {'label': 'None correct (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 4: Recall
                    html.Div([
                        html.H4("4. Delayed Recall", style={'marginBottom': '10px'}),
                        html.P("Earlier you were asked to remember three words. What were they?", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q4-recall',
                            options=[
                                {'label': 'All 3 words recalled (3 points)', 'value': 3},
                                {'label': '2 words recalled (2 points)', 'value': 2},
                                {'label': '1 word recalled (1 point)', 'value': 1},
                                {'label': 'None recalled (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 5: Language
                    html.Div([
                        html.H4("5. Language and Naming", style={'marginBottom': '10px'}),
                        html.P("Name these common objects: watch, pencil", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q5-language',
                            options=[
                                {'label': 'Both named correctly (2 points)', 'value': 2},
                                {'label': 'One named correctly (1 point)', 'value': 1},
                                {'label': 'Neither named correctly (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 6: Repetition
                    html.Div([
                        html.H4("6. Repetition", style={'marginBottom': '10px'}),
                        html.P("Repeat this phrase: 'No ifs, ands, or buts'", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q6-repetition',
                            options=[
                                {'label': 'Repeated correctly (1 point)', 'value': 1},
                                {'label': 'Incorrect (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 7: Comprehension
                    html.Div([
                        html.H4("7. Three-Stage Command", style={'marginBottom': '10px'}),
                        html.P("Take this paper in your right hand, fold it in half, and put it on the floor.", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q7-comprehension',
                            options=[
                                {'label': 'All 3 steps completed correctly (3 points)', 'value': 3},
                                {'label': '2 steps completed (2 points)', 'value': 2},
                                {'label': '1 step completed (1 point)', 'value': 1},
                                {'label': 'None completed (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 8: Reading
                    html.Div([
                        html.H4("8. Reading", style={'marginBottom': '10px'}),
                        html.P("Read and obey this: CLOSE YOUR EYES", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q8-reading',
                            options=[
                                {'label': 'Read and obeyed correctly (1 point)', 'value': 1},
                                {'label': 'Incorrect (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 9: Writing
                    html.Div([
                        html.H4("9. Writing", style={'marginBottom': '10px'}),
                        html.P("Write a complete sentence of your choice.", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q9-writing',
                            options=[
                                {'label': 'Complete, sensible sentence (1 point)', 'value': 1},
                                {'label': 'Incomplete or nonsensical (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                    # Question 10: Copying
                    html.Div([
                        html.H4("10. Visual-Spatial", style={'marginBottom': '10px'}),
                        html.P("Copy this design: [INTERLOCKING PENTAGONS]", style={'marginBottom': '10px'}),
                        dcc.RadioItems(
                            id='q10-copying',
                            options=[
                                {'label': 'Correctly copied (1 point)', 'value': 1},
                                {'label': 'Incorrect (0 points)', 'value': 0}
                            ],
                            value=None
                        )
                    ], className='question-group'),
                    
                ], style={'marginBottom': '30px'}),
                
                # Submit Button
                html.Div([
                    html.Button('Submit Cognitive Assessment', 
                               id='submit-cognitive', 
                               n_clicks=0,
                               className='btn btn-primary',
                               style={'padding': '12px 30px', 'fontSize': '16px'})
                ], style={'textAlign': 'center', 'marginBottom': '40px'}),
                
                # Results Display
                html.Div(id='cognitive-results', style={'marginTop': '30px'})
                
            ], className='card', style={'marginBottom': '40px'}),
            
            # Additional Risk Factors
            html.Div([
                html.H2("Additional Risk Factors", style={'color': '#6a46f0', 'marginBottom': '20px'}),
                
                html.Div([
                    # Family History
                    html.Div([
                        html.H4("Family History", style={'marginBottom': '15px'}),
                        dcc.Checklist(
                            id='family-history-checklist',
                            options=[
                                {'label': ' Alzheimer\'s disease in immediate family', 'value': 'alzheimers'},
                                {'label': ' Parkinson\'s disease in immediate family', 'value': 'parkinsons'},
                                {'label': ' Other dementia in immediate family', 'value': 'other_dementia'},
                                {'label': ' Stroke or vascular dementia in family', 'value': 'stroke'},
                                {'label': ' No known family history', 'value': 'none'}
                            ],
                            value=[]
                        )
                    ], className='question-group'),
                    
                    # Lifestyle Factors
                    html.Div([
                        html.H4("Lifestyle Factors", style={'marginBottom': '15px'}),
                        dcc.Checklist(
                            id='lifestyle-factors-checklist',
                            options=[
                                {'label': ' Regular physical exercise (150+ mins/week)', 'value': 'exercise'},
                                {'label': ' Mediterranean or similar healthy diet', 'value': 'healthy_diet'},
                                {'label': ' Current smoker', 'value': 'smoker'},
                                {'label': ' Heavy alcohol consumption', 'value': 'alcohol'},
                                {'label': ' Poor sleep quality (<6 hours/night)', 'value': 'poor_sleep'},
                                {'label': ' High stress levels', 'value': 'stress'},
                                {'label': ' Socially active', 'value': 'social'}
                            ],
                            value=[]
                        )
                    ], className='question-group'),
                    
                    # Medical History
                    html.Div([
                        html.H4("Medical History", style={'marginBottom': '15px'}),
                        dcc.Checklist(
                            id='medical-history-checklist',
                            options=[
                                {'label': ' High blood pressure', 'value': 'hypertension'},
                                {'label': ' Diabetes', 'value': 'diabetes'},
                                {'label': ' High cholesterol', 'value': 'cholesterol'},
                                {'label': ' Depression or anxiety', 'value': 'depression'},
                                {'label': ' Head trauma with loss of consciousness', 'value': 'head_trauma'},
                                {'label': ' Hearing loss', 'value': 'hearing_loss'},
                                {'label': ' None of the above', 'value': 'none'}
                            ],
                            value=[]
                        )
                    ], className='question-group'),
                    
                ], style={'marginBottom': '30px'}),
                
                html.Button('Save Risk Factors', 
                           id='save-factors-btn', 
                           n_clicks=0,
                           className='btn btn-secondary'),
                html.Div(id='risk-factors-output', style={'marginTop': '10px'})
                
            ], className='card', style={'marginBottom': '40px'}),
            
            # Genetic Data Analysis
            html.Div([
                html.H2("Genetic Data Analysis", style={'color': '#6a46f0', 'marginBottom': '20px'}),
                html.P("Upload your genetic data or enter SNP values for neurological risk assessment", 
                      style={'color': '#666', 'marginBottom': '20px'}),
                
                html.Div([
                    dcc.Textarea(
                        id='snp-input-assessment',
                        placeholder="Enter SNP values separated by commas (e.g., rs7412, rs429358, rs6265, rs10636)...",
                        style={
                            'width': '100%', 
                            'height': '100px', 
                            'marginBottom': '15px',
                            'padding': '12px',
                            'border': '1px solid #ddd',
                            'borderRadius': '8px',
                            'fontSize': '14px'
                        }
                    ),
                    
                    html.Div([
                        dcc.Upload(
                            id='upload-genetic-data',
                            children=html.Div([
                                'Drag and Drop or ',
                                html.A('Select Genetic File')
                            ]),
                            style={
                                'width': '100%',
                                'height': '60px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '8px',
                                'textAlign': 'center',
                                'marginBottom': '15px',
                                'cursor': 'pointer'
                            },
                            multiple=False
                        ),
                        html.Div(id='genetic-upload-output'),
                    ]),
                    
                    html.Button("Analyze Genetic Data", 
                               id='analyze-genetic-btn', 
                               n_clicks=0,
                               className='btn btn-primary',
                               style={'padding': '12px 30px'}),
                    html.Div(id='genetic-analysis-output', style={'marginTop': '20px'})
                    
                ])
            ], className='card')
            
        ], style={'maxWidth': '1000px', 'margin': '0 auto', 'padding': '20px'})
    ])