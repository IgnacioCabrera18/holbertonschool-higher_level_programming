import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return

    if template.strip() == "":
        print("Error: template is empty")
        return

    if len(attendees) == 0:
        print("Error: attendees list is empty")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation_text = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) if attendee.get(key) not in [None, ""] else "N/A"
            invitation_text = invitation_text.replace(f"{{{key}}}", str(value))

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w') as file:
                file.write(invitation_text)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")