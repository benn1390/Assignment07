#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# RBennett, 02-26-2020, Modified File per Assigment 6 Instructions
# RBennett, 03-04-2020, Modified File per Assignment 6 Feedback and Assigment 7 Instructions
#------------------------------------------#

# -- DATA -- #
import pickle
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # pickled data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def delete_inventory(ID, table): 
        """Function to delete rows of an existing table (list of Dict)


        Args:
            ID (string).

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        """
        intID = int(ID)
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intID:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return table

    @staticmethod
    def add_inventory(ID, title, artist, table): 
        """Function to add new rows to existing table (list of Dict)


        Args:
            ID (string).
            Title (string).
            Artist (string).
            table (list of dicts): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        """
        intID = int(ID)
        dicRow = {'ID': intID, 'Title': title, 'Artist': artist}
        table.append(dicRow)   
        return table

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        Includes error handling to cover situations the file to be loaded does not exist (FileNotFoundError)

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime. 
        """
        
        try: 
            objFile = open(file_name, 'rb')
            table.clear()
            table = pickle.load(objFile)
        except FileNotFoundError:
            pass
        return table

    @staticmethod
    def write_file(file_name, table):
        """Displays current inventory table
        
        Writes currently loaded data to a pickled data structure

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.

        """
        
        objFile = open(file_name, 'wb')
        pickle.dump(table, objFile)

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def add_inventory():
        """Gets user input including ID, title and artist 
        
        Includes error handling to cover situations when the user does not provide a numeric value for ID (ValueError)

        Args:
            None.

        Returns:
            ID (string): a string of the users input for CD ID number
            Title (string): a string of the users input for CD title
            Artist (string): a string of the users input for CD artist

        """
        strID = input('Enter ID: ').strip()
        while ValueError:
            try: 
                int(strID)
                break
            except ValueError:
                strID = input('Error: ID must be numeric. Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist
     
    @staticmethod
    def delete_inventory():
        """Gets user input on which CD they wish to delete.
        
        Includes error handling to cover situations when the user does not provide a numeric value for ID (ValueError)

        Args:
            None.

        Returns:
            ID (string): a string of the users input for CD ID number

        """
        strIDDel = input('Which ID would you like to delete?: ').strip()
        while ValueError:
            try: 
                int(strIDDel)
                break
            except ValueError:
                strIDDel = input('Error: ID must be numeric. Enter ID: ').strip()
        return strIDDel
 
# 1. When program starts, read in the currently saved Inventory
lstTbl = FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\n')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        strID, strTitle, strArtist = IO.add_inventory()
        # 3.3.2 Add item to the table
        lstTbl = DataProcessor.add_inventory(strID, strTitle, strArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        strIDDel = IO.delete_inventory()
        # 3.5.2 search thru table and delete CD
        lstTbl = DataProcessor.delete_inventory(strIDDel, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')




