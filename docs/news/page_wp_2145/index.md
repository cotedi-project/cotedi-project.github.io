---
title: 5 Robot Programming Challenges
author: María Zapata Cáceres
date: 2025-07-30
type: post
tags: []
hero: No image available
link: https://imaginatic.es/5-robot-programming-challenges/
...
---
Educational Experience with Robotics to Develop Computational Thinking Skills in a Secondary School: 5 Robot Programming Challenges
				
				
				
				
									
Alesio Sánchez Fernández
The study examines the importance of Computational Thinking (CT) in the educational context, particularly in developing competencies among secondary school students. It highlights how CT can help overcome educational barriers and promote inclusion, although challenges persist for students with special educational needs. The main objective is to demonstrate the effectiveness of CT, applied through robotics activities, in enhancing the skills of secondary school students, benefiting those with specific educational needs and adapting learning to be inclusive for all.
A quantitative experimental design with a pre-test and post-test was employed at IES Domenico Scarlatti in Aranjuez, involving 201 students in six sessions for the experimental group. The study concludes that there is significant learning progress among the girls in the experimental group, with notable improvements compared to their peers, although no significant progress was observed among students with special needs. The findings support the integration of CT into school curricula to prepare all students for future challenges, ensuring accessibility and equity in learning.
Dowload Educational Programme
 
 
								
				
					
				
		
					
				
				
							
			
					
						
				Introduction 			
		
				
						
				Activity design 			
		
				
						
				Implementation			
		
				
						
				Results			
		
				
						
				Conclusions			
		
				
						
				Activity Sheet			
		
					
			
				
				
				
									In the current educational context, Computational Thinking (CT) has proven to be an essential skill, with tangible benefits for students’ academic development (Zapata-Ros, 2015; Lee et al., 2011). Numerous studies support the idea that CT enhances students’ competencies, helping them to succeed in their subjects and achieve better results across various disciplines (Bocconi et al., 2016; Zapata-Cáceres & Martín-Barroso, 2021).
While academic literature has explored the impact of CT on students with high intellectual abilities and those with special educational needs separately, there remains a significant gap in understanding how this skill influences the development of students with special needs (learning difficulties, disabilities or gifted students). Therefore, it is crucial to design inclusive educational experiences that address the diversity of students found in classrooms (Buitrago et al., 2022; Frutos et al., 2012; Hontangas & de la Puente, 2010).
A practical experience was conducted to explore the relationship between CT, implemented through robotics activities, and diversity support in secondary school students. This experience encompassed a broad spectrum of students with specific educational support needs, aiming to identify the impact of CT across different levels within this spectrum. The significance of this research lies not only in understanding how CT influences students’ skill development but also in examining the variations in its impact on students with special needs.								
				
				
		
				
				
									The activity was designed to be implemented over multiple sessions with secondary school students, using mBot2 educational robots. It targeted students in Years 9, 10, and 11 (2nd, 3rd, and 4th of ESO). The necessary resources included computers with the mBlock5[1] program or the mLink2[2] connector, mBot2[3] robots, and additional materials such as printed circuits for line-following tasks. The methodology followed a quasi-experimental design, employing pre-test and post-test assessments to measure the impact of the robotics sessions on the development of Computational Thinking (CT).
Data on CT development were collected using the CTt test (Román-González, 2015; Román-González, Pérez-González & Jiménez-Fernández, 2017), which served as the evaluation instrument. The test was administered through an online form created with Microsoft Forms. Additionally, an anonymous survey was conducted to gather participants’ feedback on their experience, also using Microsoft Forms.
The specific objectives of this study are outlined below, focusing on hypothesis validation and students’ academic development:

To test the main hypothesis regarding the effectiveness of CT in improving secondary school students’ competencies, regardless of their innate abilities.
To evaluate the secondary hypothesis, which suggests that these activities have a more significant impact on students at the extremes of the NEAE spectrum.
To promote the development of CT-related skills among participating students, including abstraction, algorithmic thinking, decomposition, debugging, automation, and generalization.
To facilitate the learning of basic robotics concepts through the Scratch programming language and the use of programmable robots. Both robotics and Scratch are part of the secondary and A-level curriculum, and this study contributes to the development of these subjects.

The experience was implemented in all classes that had sufficient time available for its completion, specifically in eight secondary school classes. Figure 1 presents a schematic overview of the six sessions conducted. While the control groups participated only in Sessions 1 and 6, the experimental groups completed all sessions. Students worked in the different activities proposed during sessions 2 to 5. The first and last sessions were used to answer a questionnaire by the participants. 
 

Figure 1. Session outline
 
Specifically, the following schedule is carried out:

Initial Session


Introduction to the practical experience (5-10 minutes)
Pre-test (30-40 minutes)


Movement Session


A1: Basic movements – Drawing a simple figure with the robot’s trajectory (basic shapes) (25 minutes) (see details in Table 1).
A2: Advanced movements – Drawing a more complex figure with the robot’s trajectory (one-stroke figures) (25 minutes) (see details in Table 2).


Ultrasonic Sensor Session (A3): Avoiding obstacles to prevent collisions (20-25 minutes) (see details in Table 3).
LED Interaction Session (A4)


Displaying lights like the Knight Rider car (30 minutes) (see details in Table 4).b. Introduction to the next session and its start (20 minutes).


RGB Sensor Session (A5): Line tracking (50 minutes) (see details in Table 5).
Final Session


Post-test (30-40 minutes). Final questionnaire to validate progress.
Satisfaction survey (10 minutes). Evaluation of the experience.

The organization of the sessions in each class is done by forming 5 working groups that remain constant throughout all sessions. The groups are as balanced as possible in terms of gender and abilities, ensuring a mix of boys and girls in all groups and distributing students of different abilities. There are 5 groups because there are 5 robots for the activities, so the groups are mostly made up of 4 or 5 students, with some cases where there might be 3 or 6 students depending on the number of students in the class.
Below is the detailed list of activities to be carried out, as presented to the students, indicating the objectives, the computer skills worked on in each of them, additional information, and their solutions.

[1] https://mblock.cc/
[2] https://mblock.cc/pages/downloads
[3] https://www.makeblock.com/pages/mbot2-coding-robot
Table 1. First Activity – Basic Movements.




A1. Basic Movements: Simple Figure




Objetive


Computer skills worked on


Additional information




The robot must describe a trajectory that draws a simple geometric figure assigned to the group.
 
 
 
 


Abstraction, algorithmic thinking, and debugging.
 


Figures to be created by each work group:
·         Group 1: Square with a side length of 40 cm.
·         Group 2: Equilateral triangle with a side length of 40 cm.
·         Group 3: Rectangle with a long side of 40 cm and a short side of 20 cm.
·         Group 4: Pentagon with a side length of 30 cm.
·         Group 5: Hexagon with a side length of 25 cm.




Solution




In Figure 2, an example of a solution is shown, which works for any of the requested regular figures (square, triangle, pentagon, and hexagon), as well as for any regular figure that is to be created. One only needs to specify the number of sides (4 in the example) and the length of each side (40 in the example). In Figure 3, an example of a solution for drawing the rectangle is shown. These solutions are general, allowing for easy modification of the result, but students typically use the simpler method of indicating repetitions and values directly in the instructions.

Figure 2. Basic Movements: Simple Figure. Solution for regular figures.

Figure 3. Basic Movements: Simple Figure. Solution for the rectangle activity.




Table 2 – Second Activity – Advanced Movements.




A2. Advanced Movements: Complex Figure




Objetive


Computer skills worked on


Additional information




The robot must describe a trajectory that draws a single-stroke figure assigned to the group.


Abstraction, algorithmic thinking, and debugging.


Figures to be created by each work group. Figure 4 presents the assignment of more complex geometric figures to each work group with the goal of working on more advanced movements.




Solution




For this exercise, it is ideal for students to plan the movements on paper first and then transfer them to the program. They should first think about the solution to the problem and then figure out how to implement it in the program.

Figure 4. Geometric Figures for Working on Advanced Movements with the Robot.




Table 3 – Third Activity – Avoiding Obstacles.




A3. Ultrasonic Sensor: Avoiding Obstacles




Objetive


Computer skills worked on


Additional information




The robot must avoid any obstacles it encounters in its path.


Abstraction, algorithmic thinking, decomposition, and debugging.


§  Detect at a certain distance.
§  Use the «Forever» block.
§  Choose what to do when an obstacle is detected.




Solution




Figure 5 shows an example of a solution for this activity. Typically, students make the robot turn in the same direction whenever an obstacle is encountered. Once this is achieved, they can be asked to make the robot turn randomly to either side, with a different turning angle each time.
 
Figure 5 – Solution to Activity 3: Avoiding Obstacles.




Table 4 – Fourth Activity – LEDs as «Knight Rider» Kit.




A4. LEDs: «Kit» Light (Knight Rider Car)




Objetive


Computer skills worked on


Additional information




It must display the back-and-forth movement of lights like the Knight Rider car, similar to the one shown in Figure 6.

Figure 6. Image of the Knight Rider car lights.Fuente: qkbestet.pics


Abstraction, algorithmic thinking, automation, and decomposition.  


Figures to be created by each work group:
·         Use the «LED» instruction block.
·         Start with the movement of a single LED, aiming for a smooth motion.




Solution




Figure 7 shows a simple solution, for example, moving 2 LEDs without leaving a trail. Typically, students begin by initializing the light to display each time (the first one that appears in the figure after pressing button B) in a different position. This solution is not very effective, so the next step is to ask them to create a code that can be easily modified to be valid for any length of the LED strip, not just the 5-LED strip shown. An additional improvement for more advanced students would be to try doing it while viewing the trail.

Figure 7 – Solution to Activity 4: Kit Light.




Table 5 – Fifth Activity – Line Following.




A5. RGB Sensor: Line Following




Objetive


Computer skills worked on


Additional information




The robot must find the black line and continuously follow it along the entire path.


Abstraction, algorithmic thinking, decomposition, debugging, automation, and generalization.


There are 4 sensors in the mBot2, as shown in Figure 8. The L1 and R1 sensors must be used.

Figure 8. RGB Sensors of the mBot2.
Use the «Forever» block. 
Use «detect line» in the instructions instead of detecting a specific color. 
Pay attention to the motor rotation direction if that instruction is used. See the direction of rotation for each wheel in Figure 9.

Figure 9. Direction of Motor Rotation in the mBot2.
Use logical operations according to the 4 detection states of the 2 sensors with the line, as indicated in Figure 10.

Figure 10. Logical Operations of the 4 States. Source: Author’s own creation.




Solution




Figure 11 shows a simple solution for this activity. Typically, students start by making small 1° turns for the curves and then check again. This causes the robot to spin in place, giving no sense of forward motion in the curves. Once this is achieved, they can be asked to make the curves smoother, allowing the robot to maintain its sense of forward progress. Finally, they could do it at a higher speed and perform some action upon detecting a color on the line.

Figure 11 – Solution to Activity 5: Line Following.




 
 
 
 
 
 
 								
				
				
		
				
				
									The experience was carried out at the IES Domenico Scarlatti in Aranjuez, Madrid, during the 2023/2024 academic year, with the participation of 201 students. The students were divided into control and experimental groups, with the experimental group carrying out the robotics sessions. The sessions took place in classrooms equipped for this purpose and were conducted in collaborative work groups. The student population included students with specific educational support needs.
The control group consisted of 84 participants from 2nd and 3rd year of Secondary Education (ESO), while the experimental group included 117 participants from 2nd, 3rd, and 4th year of ESO. The classes belonging to the control and experimental groups were the students’ natural classes and were selected by the educational center itself.
As the participants were minors, explicit consent was obtained through signed permission from the students’ parents or guardians to conduct the study. Furthermore, this study has been authorized by the Research Ethics Committee of the Rey Juan Carlos University, with registration number 281120234182023								
				
				
		
					
				
				
									The main results of the activity showed that the experimental group experienced meaningful learning in computer skills, particularly among girls (Wilcoxon test; p = 0.0003031), who showed significant improvements compared to their male peers and the control group (boys in the experimental group: p = 0.8316; boys in the control group: p = 0.7588; girls in the control group: p = 0.8644). These findings suggest that meaningful learning in the experimental group occurred primarily among the girls. Figure 12 visually displays these results, where the means of the control and experimental groups, segmented by gender, can be observed in the pre- and post-tests of the experience.

Figure 12. Graph showing the means of the control and experimental groups segmented by gender.
 
In the analysis of the NEAE subgroup, consisting of 10 students in the control group and 14 in the experimental group, the Wilcoxon test for paired samples was used due to the small sample size (less than 35). This method is appropriate for evaluating differences in measurements taken at two different time points.
The results indicate that no significant improvements were observed in the performance of special needs students in either group (p = 0.4136 in the experimental group and p = 0.7907 in the control group). These findings suggest the need for a more in-depth analysis to identify potential patterns or effects that might not be evident through conventional statistical tests. An additional approach could reveal subtle influences that, although not statistically significant, may have pedagogical relevance.
These conclusions support the integration of computer skills activities into school curricula as an essential tool for improving students’ competencies.								
				
					
				
		
					
				
				
									The activity demonstrated that robotics sessions can be effective in developing computer skills in Secondary Education (ESO) students, particularly among girls. Although no significant improvements were found in students with special needs, the activity provides a solid foundation for future research and adjustments in the design of activities to enhance their inclusion and effectiveness. It is essential to continue exploring and adapting these activities to ensure that all students can benefit from them.
 
Funding
The materials for the execution of this activity have been funded by the Erasmus+ CoTEDI project, which is funded by the European Union under Key Action 2023-1-NL01-KA220-SCH-000152037 – OID E10207981.
 
Acknowledgements
I would like to thank my TFM supervisors, Estefanía Martín Barroso and María Zapata Cáceres, for their support and guidance throughout the development of this project.
 
References
Bocconi, S., Chioccariello, A., Giuliana, D., Ferrari, A., & Engelhardt, K. (2016). Developing Computational Thinking in Compulsory Education – Implications for policy and practice. JRC Research Reports JRC104188, Joint Research Centre. Handle: RePEc:ipt:iptwpa:jrc104188.
Buitrago, L. M., Laverde, G. M., Amaya, L. Y., & Hernández, S. I. (2022). Pensamiento computacional y educación STEM: Reflexiones para una educación inclusiva desde las prácticas pedagógicas. Panorama, 16(30), pp. 233-257. DOI: 10.15765/pnrm.v16i30.3134.
Frutos, A. E., Ruíz, A. B. M., Sánchez, J. J. M., Rus, T. I., Hidalgo, J. I. L., Sánchez, N. O., & Martín, M. S. (2012). La atención a la diversidad: la educación inclusiva. Revista Electronica Interuniversitaria de Formación del Profesorado, 15(1), pp. 135-144. Disponible en: https://bit.ly/3FmUPYw.
Hontangas, N. A., & de la Puente, J. L. B. (2010). Atención a la diversidad y desarrollo de procesos educativos inclusivos. Prisma social, (4), pp.1-37. Disponible en: https://bit.ly/3FlHK1o.
Lee, I., Martin, F., Denner, J., Coulter, B., Allan, W. C., Erickson, J., Malyn-Smith, J., & Werner, L. (2011). Computational Thinking for Youth in practice. ACM Inroads, 2(1), pp. 32-37. DOI: 10.1145/1929887.1929902
Román González, M. (2015). Computational thinking test: Design guidelines and content validation. In EDULEARN15 Proceedings, pp. 2436-2444. IATED. DOI: 10.13140/RG.2.1.4203.4329
Román-González, M., Pérez-González, J., & Jiménez-Fernández, C. (2017). Which cognitive abilities underlie computational thinking? Criterion Validity of the Computational Thinking test. Computers in Human Behavior, 72, pp. 678-691. DOI: 10.1016/j.chb.2016.08.047
Zapata-Cáceres, M., & Martín, E. (2021). Applying Game Learning Analytics to a Voluntary Video Game: Intrinsic Motivation, Persistence, and Rewards in Learning to Program at an Early Age. IEEE Access, 9, pp. 123588-123602. DOI: 10.1109/access.2021.3110475
Zapata-Ros, M. (2015). Pensamiento computacional: Una nueva alfabetización digital. RED. Revista de Educación a Distancia, 46. DOI: 10.6018/red/46/4								
				
					
				
		
					
				
				
									



EP title


Educational experience with robotics to develop Computational Thinking skills in a secondary school




Author


Alesio Sánchez Fernández




Name of Educational Center


IES Domenico Scarlatti




Status


Done




Start Date


08/01/2024




End Date


23/02/2024




Target groups




Age range of students


12-15




Grade level


ESO (secondary education)




Number of students involved


201




Educational context


Computer room with computers




Diversity


Includes 24 participants with special needs: learning difficulties, disabilities and high cognitive abilities.




Required resources




WiFi connection is required


Yes




Devices


Computers and mBot2 educational robots.




Tangible materials


Printed circuit on paper for line tracking.




Activity description




Activity Description


The educational program consists of 5 activities:
§  Draw a simple figure with the robot’s movement.
§  Draw a complex figure with the robot.
§  Avoid obstacles using the ultrasonic sensor.
§  Use the LEDs to simulate the light of the «Knight Rider» car kit.
§  Line tracking with the RGB sensor.
The details of these activities have been included in the activity design section of this document.




Total time needed


4 classes for the robotics activities and another two classes to complete the computational thinking tests. The details can be seen in the planning of Figure 1.




Subject(s)


Technology and Digitalization.




Specific topic addressed


Abstraction, algorithmic thinking, decomposition, debugging, automation, and generalization.




Plugged / Unplugged


Plugged (robots)




Type of Activity


Educational robotics with Scratch-based programming environment




Individual / Collaborative.


Collaborative: groups of 3 to 6 members




Level of creativity


Low




Level of technology


Medium




Computational skills worked and how they are developed


§  Abstraction
§  Pattern recognition
§  Problem decomposition
§  Generalization
§  Algorithmic thinking
§  Evaluation
§  Error detection




Activity protocol and guidelines 




Activity Protocol and Guidelines


The activity followed a structured process that included problem analysis, identification of the robot’s instructions and functions, and solution design. Students engaged in block-based programming to implement their solutions, followed by practical testing with the robot to observe its behaviour. They also performed error debugging and made applicable improvements based on test results. Each activity was allocated 50 minutes, except for the two figure-drawing activities, which together took a total of 50 minutes.




Teacher Training


Knowledge of Scratch is required, and general knowledge of robots is recommended.




Inclusion




Adaptation for Special Needs


No special adaptations have been made to the activities, but they would be advisable. In the case of high-ability students, a greater challenge would be recommended by increasing the complexity of the activity itself. In the case of students with special educational needs, adaptations should be made according to each student’s specific needs, dedicating more time, providing more detailed explanations, etc.




Additional details




The main problems identified have been: 
§  Lack of attention and understanding. 
§  Low capacity for abstraction. 
§  Difficulty in refining and building on acquired experience. 
The proposed improvements are: 
§  Adaptations of activities for gifted students and students with learning difficulties. 
§  Extending the duration of activities (number of sessions and number of tasks). 
§  Smaller working groups (preferably individual work) and more suitable classrooms.
