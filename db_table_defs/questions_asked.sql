create table questions_asked(
    question_id UUID PRIMARY key,
    bill_id UUID not null,
    asked_user_id UUID,
    created_at timestamptz not null default now(),
    question varchar,
    answer varchar,
    suspected_dupe bool default false,
    dupe_of_question_id UUID,
    confirmed_dupe bool default false
);