This is my first script language with the aim of implementing the knowledge acquired in Python. It has primarily served as a learning tool for Python and reflects my knowledge of bash/Python exclusively in the first semester of M1 bio-informatic/biostatistic. The project idea and its structure (the role of each file) are the work of the instructor Frederic Goualard. However, no programming/algorithmic instructions were given, and this field was open.

The purpose of this program is to allow the user to locate the nearest parking lots, along with their rates, based on an address in Nantes, and enable the user to choose the minimum number of available spaces they desire. It should be used from a Linux terminal using the command:
./jemegare.sh <address> <integer=parking duration> <integer=minimum parking spaces> <integer=list size>.

Example: ./jemegare.sh "13 rue du yonep" "60" "20" "5"

Based on these instructions, the user will see a list of parking lots displayed on the terminal, starting with the one closest to their location, along with the expected price based on the desired duration of stay.

The parking rates list is updated every 30 days, and the availability of parking spaces is updated every hour from the website. https://data.nantesmetropole.fr/pages/home/

