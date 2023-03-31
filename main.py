import pip
import urllib.request
import urllib.parse
import sys
import os
import http.client
from dotenv import load_dotenv

load_dotenv()

username = None
password = None
student_id = None


def user_input():
    global username, password, student_id

    try:
        username = sys.argv[1]
        password = sys.argv[2]
        student_id = sys.argv[3]
    except:
        username = os.environ.get('USIS_USERNAME')
        password = os.environ.get('USIS_PASSWORD')

        if username is None or password is None:
            username = input('Enter USIS Username: ')
            password = input('Enter USIS Password: ')
            student_id = input('Enter Student ID: ')
        else:
            try:
                student_id = sys.argv[1]
            except:
                student_id = input('Enter Student ID: ')


def main():
    user_input()

    filename = f'GRADE_SHEET_{student_id}.pdf'

    if len(student_id) != 8:
        return print('Invalid Student ID')

    try:
        # Options
        academic_standing = 'Poltibaaj'
        company_logo = 'https://i.pinimg.com/originals/23/29/fd/2329fdc98e26126dfd67e77a71b82c91.png'
        # company_logo = '%2Fvar%2Facademia%2Fimage%2FuniversityLogo%2F1571986355.jpg'
        company_name = 'BRAC+University'
        header_title = 'GRADE+SHEET'
        company_address = 'LAUGH+TALE%2C+NEW+WORLD'
        # company_address = '66%2C+MOHAKHALI+C%2FA%2C+DHAKA+-+1212.'
        # If you want your own watermark, upload it to dadeviantart and copy the image link
        grade_sheet_background = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f59a072a-716c-4ab8-892a-03015395727e/dfsxhru-bd49728b-7587-4867-bbc4-42f64b6deab0.jpg/v1/fill/w_1280,h_1811,q_75,strp/one_piece_by_testypotato2_dfsxhru-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTgxMSIsInBhdGgiOiJcL2ZcL2Y1OWEwNzJhLTcxNmMtNGFiOC04OTJhLTAzMDE1Mzk1NzI3ZVwvZGZzeGhydS1iZDQ5NzI4Yi03NTg3LTQ4NjctYmJjNC00MmY2NGI2ZGVhYjAuanBnIiwid2lkdGgiOiI8PTEyODAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.cfvZEL3-CWsdsDsLkXJm6M1e8Hp4apX_OtaKXV4jAKA"
        # grade_sheet_background = '%2Fbits%2Fusis%2Ftomcat%2Fwebapps%2Facademia%2Fimages%2FgradeSheetBackground.jpg'

        # Build the URL using the variables
        file_url = f'https://usis.bracu.ac.bd/academia/docuJasper/index?studentId={student_id}&reportFormat=PDF&old_id_no={student_id}&strMessage=&scholarProgramMsg=&companyLogo={company_logo}&companyName={company_name}&headerTitle={header_title}&companyAddress={company_address}&academicStanding={academic_standing}&gradeSheetBackground={grade_sheet_background}&_format=PDF&_name={filename}&_file=student%2FrptStudentGradeSheetForStudent.jasper'
        login_url = 'https://usis.bracu.ac.bd/academia/j_spring_security_check'

        conn = http.client.HTTPSConnection("usis.bracu.ac.bd")
        payload = f'j_username={username}&j_password={password}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://usis.bracu.ac.bd',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://usis.bracu.ac.bd/academia/',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }
        conn.request("POST", "/academia/j_spring_security_check", payload, headers)
        res = conn.getresponse()
        session_id = res.getheader('Set-Cookie')
    except Exception as e:
        print('Error while login:', e)

    try:
        request = urllib.request.Request(file_url, headers={'Cookie': session_id})
        with urllib.request.urlopen(request) as response, open(filename, 'wb') as file:
            file.write(response.read())
            print('File downloaded as:', filename)

        # Open the file
        if sys.platform == 'win32':
            os.startfile(filename)  # This works on Windows
        else:
            opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
            os.system(f'{opener} {filename}')  # This works on macOS and Linux

    except Exception as e:
        print('Error while downloading:', e)


def clean_terminal():
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")


if __name__ == '__main__':
    clean_terminal()
    main()
