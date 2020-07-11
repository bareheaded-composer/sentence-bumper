# Sentence Bumper

Sentence Bumper bumps sentences from [hitokoto-osc/sentences-bundle](https://github.com/hitokoto-osc/sentences-bundle).

## Setup and Basic Usage

``` sh
$ git clone https://github.com/bareheaded-composer/sentence-bumper.git sentence-bumper
$ cd sentence-bumper

$ git clone https://github.com/hitokoto-osc/sentences-bundle.git data/hitokoto-osc-sentences-bundle

$ python3 sentence_bumper
{
  "id": 4114,
  "uuid": "707fbfe2-b839-4e90-9c17-f25bbacf5a98",
  "hitokoto": "程序漏洞叫特性，设计漏洞叫特色",
  "type": "e",
  "from": "沃·兹基·硕得",
  "from_who": null,
  "creator": "语冰夏虫",
  "creator_uid": 2263,
  "reviewer": 0,
  "commit_from": "web",
  "created_at": "1540725706",
  "length": 15
}

# Run `python3 sentence_bumper --help` to discover more options.
```

## License

The Unlicense

Please be aware that [hitokoto-osc/sentences-bundle](https://github.com/hitokoto-osc/sentences-bundle) is AGPLv3.
