select
	sessions.id as SeshID,
	sessions.psiturkWorkerId as WorkerID,
	sessions.startTime as StartTime,
	sessions.stopTime - sessions.startTime as Duration,
	sessions.exitSurvey as ExitSurvey,
	count(ratings.id) as NumRatings
from sessions
inner join ratings on ratings.sessionId = sessions.id
inner join stimuli on ratings.stimulusId = stimuli.id
inner join psiturk on sessions.psiturkUid = psiturk.uniqueid
where
	sessions.wave in (%s)
	and psiturk.status >= 3
	and (psiturk.mode is null or psiturk.mode = "live")
	and sessions.id not in (
		select
			sessions.id
		from sessions
		inner join ratings on sessions.id = ratings.sessionId
		inner join stimuli on ratings.stimulusId = stimuli.id
		group by
			sessions.id,
			stimuli.duration
		having
			(stimuli.duration - max(ratings.pollSec)) >= 80
	)
group by
	sessions.id
order by
	StartTime
;
