import os
from crewai import Agent, Task, Crew, LLM

def generate_prd(target_app, crux_context):
    """
    Takes the distilled insights (Crux) from processor.py 
    and generates a final PRD.
    """
    
    # Corrected Model ID for Gemini 2.0 Flash
    # The 'gemini/' prefix is required for CrewAI to use the Google SDK
    pm_llm = LLM(
        model="gemini/gemini-2.0-flash", 
        api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.2 # Lower temperature for more structured PRD output
    )

    # 1. Define the PM Agent
    pm = Agent(
        role='Senior Product Manager',
        goal=f'Create a technical PRD for {target_app} based on processed user insights.',
        backstory="""You specialize in converting raw customer pain points into 
        structured engineering requirements. Your PRDs are known for being 
        concise, actionable, and data-driven.""",
        llm=pm_llm,
        verbose=True
    )

    # 2. Define the Task
    # Note: 'crux_context' is the output from your processor.py
    task = Task(
        description=f"""The user feedback for {target_app} has been processed into a 'Crux' summary.
        
        CRUX SUMMARY:
        {crux_context}
        
        Your task is to:
        1. Convert these insights into a formal Product Requirements Document (PRD).
        2. Include sections for: Overview, User Stories, Feature Requirements, and Success Metrics.""",
        expected_output="A professionally formatted Markdown PRD.",
        agent=pm
    )

    # 3. Kickoff the Crew
    return Crew(agents=[pm], tasks=[task]).kickoff()