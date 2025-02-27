##############################################   Title of your research project   ########################################
"Optimizing Matrix Inversion with Advanced Prompt Engineering"

###############################################  1-liner description of your project  #########################################
Exploring the efficiency of various prompt engineering techniques for computing matrix inversion using LLMs.

Authors: NAME1:Jahnavi Vajrala, NAME2:Hari Venkata Ravi Teja Anumukonda , NAME3:Likhitha Talluru
Academic Supervisor: Dr. Fernando Koch

##Research Question##
How can different prompt engineering techniques enhance the accuracy, efficiency, and descriptiveness of matrix inversion computations using LLMs?

################################################### Arguments #########################################################

########    What is already known about this topic

You could use prompt engineering techniques to achieve efficient and accurate matrix inversion computations.
The challenges of balancing response time with descriptive depth in LLM outputs.
The possibility of optimizing prompt structures to improve both accuracy and speed.

########    What this research is exploring
We employ Chain-of-Thought (CoT), Zero-Shot, and Prompt-to-Prompt techniques.
We are building a comparative analysis of their effectiveness in computing matrix inversion.
We are exploring how different prompt structures impact response quality, speed, and depth of explanation.

########    Implications for practice
It will be easier to choose the right prompt engineering technique based on computational needs.
It will optimize LLM-based numerical problem-solving, reducing computational time while maintaining accuracy.
We will better understand how prompt structures influence reasoning capabilities in AI models.


################################################### Research Method ##############################################

We conducted matrix inversion tasks using the Mistral:latest model with three different prompt engineering techniques:

Chain-of-Thought (CoT): Delivered the most detailed and structured answers in 110 seconds.
Zero-Shot: Produced accurate but less descriptive results in 48 seconds.
Prompt-to-Prompt: Provided the best balance of speed and accuracy, computing results in just 17 seconds.
We analyzed response quality, depth, and computational time to determine the optimal technique.

####################################################  Results  #################################################

CoT excelled in structured and detailed explanations but had the longest execution time (110s).
Zero-Shot provided a quick and accurate result (48s) but lacked depth in explanation.
Prompt-to-Prompt was the fastest (17s) while maintaining high accuracy and decent explanation quality.


################################################  Further research  ##############################################
Exploring hybrid techniques that combine CoT and Prompt-to-Prompt for better efficiency.
Evaluating other LLM models beyond Mistral for similar tasks.
Investigating parameter tuning (e.g., temperature, max tokens) to further optimize performance.