# Job-shop-scheduling-problem
This is a 10x10 Job shop problem. There are 10 workpieces and 10 machines. Each workpiece is processed in a different order on each machine. The scheduling goal is to minimize the total completion time (Makespan). The data is based on the workpiece. The sequence of processing operations is presented. Each workpiece will go through 10 processing operations. The following table records the processing machine and processing time required for each workpiece in each processing operation.

### Processing_time
![image](https://github.com/Eason0227/Job-shop-scheduling-problem/assets/102510341/7d659a7e-56d0-4358-9de8-e0eee07b55b2)
### Machine_sequence
![image](https://github.com/Eason0227/Job-shop-scheduling-problem/assets/102510341/5f8e811f-b7ec-4df4-a445-956a7c154ace)
## Genetic Algorithm result
* best makespan: 884, runnning time: 5min 53s  
* Gantt chart
![newplot](https://github.com/Eason0227/Job-shop-scheduling-problem/assets/102510341/4c292a21-b71e-463b-894b-10cd40579e17)

## PULP result
* A pcakage for solving mathematical programming in Python, which can solve linear programming, integer programming, and mixed integer programming problems
* Optimal makespan :  838.0 , runnning time: 26min 36s  
* Gantt chart  
![pulp ](https://github.com/Eason0227/Job-shop-scheduling-problem/assets/102510341/0a7b1d3d-8881-4e7b-9665-952801ef6bc7)
