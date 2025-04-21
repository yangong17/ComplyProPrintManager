# ComplyPro Label Printing Manager

### Overview  
The ComplyPro Label Printing Manager is a Python-based tool designed to extend the capabilities of the Certags ComplyPro Label Designer program. It enables users to queue up and print multiple label files in a single operation, streamlining the printing process and eliminating the need to manually print label files individually.

In typical manufacturing workflows, operators may need to print labels for dozens or even hundreds of unique parts—such as hoses, cables, or assemblies - where each file must be opened and printed individually. For a project with 200 labels, this results in approximately 50 minutes of manual processing (based on recorded benchmarks). This tool reduces that task to a quick setup, allowing printing to run unattended—freeing up operator time and reducing errors.

### Key Use Case in Manufacturing  
- Ideal for labeling operations involving many different part numbers  
- Reduces operator burden and the risk of label mix-ups during high-volume print runs  
- Frees up labor for higher-value activities during unattended batch printing  

### Return on Investment (ROI)  
**Example scenario:**  
- 200 label files to print  
- Manual printing:  
  - 10 seconds to print × 200 = 2000 seconds  
  - 5 seconds to switch files × 199 = 995 seconds  
  - **Total operator time: 2995 seconds (~49 minutes 55 seconds)**  
- Automated with this tool:  
  - ~60 seconds setup  
  - **Total operator time: ~1 minute**

**Time saved:** ~48 minutes 55 seconds  
**Reduction in required operator time: ~98%**

By automating the label printing process, manufacturers significantly reduce labor overhead while improving consistency and throughput. This is especially valuable for high-mix production where manual label changes are frequent and time-consuming.

### Features  
- Batch printing of multiple label files in one operation  
- Simple and intuitive user interface  
- Real-time logging of print progress  
- Emergency stop via 'Esc' key  

### Requirements  
- Python 3.x  
- Python libraries:  
  - `pygetwindow`  
  - `pyautogui`  
  - `keyboard`  
(Install dependencies using `requirements.txt`)

### Usage  
1. Start the ComplyPro Label Designer.  
2. Launch the ComplyPro Label Printing Manager.  
3. Use the 'Select Files' button to choose label files.  
4. Set the print quantity for each label.  
5. Click 'Print Labels' to begin batch printing.  
6. Monitor progress through the real-time log. Press 'Esc' to cancel at any time.

### License  
MIT License

### Contact  
For support or questions, contact: yzong17@gmail.com

---

Let me know if you'd like this exported to PDF or included with sample screenshots for internal documentation.
