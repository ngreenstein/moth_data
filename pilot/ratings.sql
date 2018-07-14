select
	ratings.id as RateID,
	ratings.sessionId as SeshID,
	psiturk.workerid as ParticipantID,
	stimuli.filename as StimName,
	stimuli.id as StimID,
	ratings.pollSec as PollSec,
	ratings.sliceStartSec as SliceStartSec,
	ratings.reactionTime as ReactionTime,
	ratings.intensities as Ratings
from ratings
inner join stimuli on ratings.stimulusId = stimuli.id
inner join sessions on ratings.sessionId = sessions.id
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
order by
	StimID asc,
	SeshID asc,
	PollSec asc
;
