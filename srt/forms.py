from django import forms



class TrainSearchForm(forms.Form):
    departure_station = forms.ChoiceField(choices=[('울산(통도사)', '울산(통도사)'), ('수서', '수서'), ('동대구', '동대구')], label='출발 역')
    arrival_station = forms.ChoiceField(choices=[('울산(통도사)', '울산(통도사)'), ('수서', '수서'), ('동대구', '동대구')], label='도착 역')
    departure_time_from = forms.TimeField(label='출발 시간(시작)')
    departure_time_to = forms.TimeField(label='출발 시간(종료)')
    date = forms.DateField(label='출발 일자')