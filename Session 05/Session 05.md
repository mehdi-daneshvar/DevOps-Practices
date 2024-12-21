# DevOps Exercises

---

## **Session 5: Docker Installation Methods and Linux Namespaces**

### **Student Name:** Mehdi Daneshvar

### **Date:** September 19, 2024

---

**1. [What is the difference between installing Docker from Debian's repositories and Docker's own repositories?](#1--what-is-the-difference-between-installing-docker-from-debians-repositories-and-dockers-own-repositories)**  
**2.[Types of namespaces in Linux and an explanation of each](#2--types-of-namespaces-in-linux-and-an-explanation-of-each)**

### **1- What is the difference between installing Docker from Debian's repositories and Docker's own repositories?**

1. **Source of Packages**:  
   - **Debian's Repositories**: Packages are provided by Debian, tested for compatibility, but may be outdated.  
   - **Docker's Own Repositories**: Maintained by Docker, offering the latest features and updates.  

2. **Version Updates**:  
   - **Debian's Repositories**: Updates follow Debian's release cycles, which may delay access to new features.  
   - **Docker's Own Repositories**: Updates are more frequent and aligned with Docker’s latest developments.  

3. **Compatibility**:  
   - **Debian's Repositories**: Ensures stability within the Debian ecosystem.  
   - **Docker's Own Repositories**: Designed for multiple distributions, requiring manual repository configuration.  

4. **Ease of Installation**:  
   - **Debian's Repositories**: Straightforward with default package manager.  
   - **Docker's Own Repositories**: Involves additional setup but provides advanced tools like the latest Docker Compose.  

---

### **2- Types of Namespaces in Linux and an Explanation of Each**

1. **Mount (`mnt`)**:  
   - Isolates file system mount points, allowing independent filesystem views.

2. **Process ID (`pid`)**:  
   - Isolates process IDs, enabling separate process trees.

3. **Network (`net`)**:  
   - Isolates network stack, providing independent IP addresses and interfaces.

4. **User (`user`)**:  
   - Isolates user and group IDs, supporting ID mapping between namespace and host.

5. **UTS (`uts`)**:  
   - Isolates system identifiers like hostname and domain name.

6. **IPC (`ipc`)**:  
   - Isolates inter-process communication mechanisms like shared memory.

7. **Cgroup**:  
   - Isolates resource control groups, limiting visibility and access to host resources.  
